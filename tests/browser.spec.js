const { test, expect } = require('@playwright/test');
const AxeBuilder = require('@axe-core/playwright').default;
const article = '/blog/bombay-house-tata-board-graph/';
const old = '/blog/Bytecode-Instrumentation-with-ASM-Modifying-Java-and-Scala-Without-Touching-the-Code/';
const finance = '/blog/discounted-cash-flows-the-math-part-1/';
const longTitle = '/blog/Understanding-Linux-cgroups-The-Foundation-of-Resource-Isolation-in-LXC-date-2017-02-10-author-Ganesh-Raman-tags-linux,-containers,-lxc,-cgroups,-system-internals,-kernel,-process-isolation-categories/';
test.beforeEach(async ({page}) => { await page.route('https://giscus.app/**', route => route.abort()); });
async function noOverflow(page) { expect(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth)).toBeTruthy(); }
for (const width of [320,390,768,1280]) {
  test(`reading, layout and accessibility at ${width}px`, async ({page}, info) => {
    await page.setViewportSize({width,height:900});
    for (const path of ['/',article,old,finance,longTitle,'/search/','/series/']) {
      await page.goto(path); await expect(page.locator('main h1')).toBeVisible(); await noOverflow(page);
      const result=await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21aa']).analyze();
      expect(result.violations,JSON.stringify(result.violations.map(v=>({id:v.id,nodes:v.nodes.map(n=>n.target)})))).toEqual([]);
    }
    await page.goto(article); await page.screenshot({path:info.outputPath(`article-${width}.png`)});
    if(width===1280) {
      const measure=await page.locator('.page__content').evaluate(el=>el.getBoundingClientRect().width);
      expect(measure).toBeLessThanOrEqual(760); expect(measure).toBeGreaterThanOrEqual(650);
    }
    if(width<800) {
      await page.locator('.mobile-nav summary').click(); await expect(page.locator('.mobile-nav a').first()).toBeVisible();
      await page.keyboard.press('Escape'); await expect(page.locator('.mobile-nav')).not.toHaveAttribute('open','');
    }
    await page.locator('.reading-toc summary').click(); await expect(page.locator('.reading-toc nav')).toBeVisible();
    await page.locator('.reading-toc a').first().click(); expect(new URL(page.url()).hash).toBeTruthy();
    const table=page.locator('.table-scroll').first(); await table.focus(); await expect(table).toBeFocused();
    await table.press('ArrowRight'); await noOverflow(page);
    await page.goto(old); await expect(page.locator('pre').first()).toBeVisible(); await page.locator('pre').first().focus(); await expect(page.locator('pre').first()).toBeFocused();
    const codeSizes=await page.locator('.page__content code').evaluateAll(elements=>elements.map(el=>parseFloat(getComputedStyle(el).fontSize)));
    expect(Math.min(...codeSizes)).toBeGreaterThanOrEqual(14);
    await page.goto('/'); await page.screenshot({path:info.outputPath(`home-${width}.png`),fullPage:true});
  });
}
test('body snippets, topic filters, query history, reset and empty states',async ({page},info)=>{
  await page.goto('/search/'); await page.getByLabel('Search the notebook',{exact:true}).fill('terminal value');
  await expect(page.locator('#search-status')).toHaveAttribute('data-query','terminal value');
  await expect(page.locator('#search-status')).toContainText('articles found');
  await expect(page.locator('#search-results')).toContainText('terminal');
  await expect(page.locator('#search-results')).not.toContainText('Series map:');
  await page.getByLabel('Topic',{exact:true}).selectOption({label:'Finance & corporate networks'});
  await expect(page.locator('#search-status')).toContainText('articles found');
  expect(page.url()).toContain('topic=');
  await page.getByRole('button',{name:'Reset search'}).click();
  await expect(page.locator('#search-status')).toContainText('Enter a word');
  await page.goBack(); await expect(page.locator('#search-query')).toHaveValue('terminal value');
  await expect(page.locator('#search-status')).toContainText('articles found');
  await page.goForward(); await expect(page.locator('#search-query')).toHaveValue('');
  await page.locator('#search-query').fill('qwertyqwerty'); await expect(page.locator('#search-status')).toContainText('No articles found');
  await page.getByRole('button',{name:'Reset search'}).click();
  for(const query of ['Kafka','Haskell','board interlocks','cgroups','CAPM','Tata','S3','Git as a Distributed System','NumPy']) {
    await page.locator('#search-query').fill(query); await expect(page.locator('#search-status')).toHaveAttribute('data-query',query); await expect(page.locator('#search-status')).toContainText(/article[s]? found/);
    await expect(page.locator('.search-result').first()).toBeVisible();
  }
  await page.screenshot({path:info.outputPath('search.png'),fullPage:true});
});
test('separate series navigation, keyboard and reduced motion',async({page})=>{
  await page.emulateMedia({reducedMotion:'reduce'}); await page.goto(finance);
  await expect(page.getByRole('navigation',{name:'Series navigation'})).toContainText('Next in this series');
  await expect(page.getByRole('navigation',{name:'Chronological post navigation'})).toContainText('Later in the archive');
  await page.keyboard.press('Tab'); await expect(page.getByRole('link',{name:'Skip to primary navigation'})).toBeFocused();
  await page.keyboard.press('Tab'); await page.keyboard.press('Enter'); await expect(page.locator('main')).toBeInViewport();
  expect(await page.locator('.masthead').evaluate(el=>getComputedStyle(el).animationName)).toBe('none');
});
test('no-JavaScript reading, mobile menu, contents and archive navigation',async({browser,baseURL})=>{
  const context=await browser.newContext({baseURL,javaScriptEnabled:false,viewport:{width:320,height:740}});
  const page=await context.newPage(); await page.goto(article);
  await noOverflow(page); await expect(page.locator('.page__content')).toContainText('Bombay House');
  await page.locator('.reading-toc summary').click(); await expect(page.locator('.reading-toc nav')).toBeVisible();
  await page.locator('.mobile-nav summary').click(); await page.locator('.mobile-nav').getByRole('link',{name:'Writing',exact:true}).click();
  await expect(page.locator('h1')).toHaveText('Writing');
  await page.goto('/search/'); await expect(page.getByRole('link',{name:'browse topics',exact:true})).toBeVisible(); await page.getByRole('link',{name:'browse topics',exact:true}).click(); await expect(page.locator('h1')).toHaveText('Topics'); await context.close();
});
test('200% zoom equivalent reflow and long title',async({page},info)=>{
  // A 1280px viewport at 200% zoom exposes 640 CSS pixels (WCAG reflow test).
  await page.setViewportSize({width:640,height:450}); await page.goto(longTitle); await noOverflow(page);
  await expect(page.locator('h1')).toBeVisible(); await expect(page.locator('.mobile-nav summary')).toBeVisible();
  await page.screenshot({path:info.outputPath('200-percent-reflow.png'),fullPage:true});
});
