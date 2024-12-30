import asyncio
from pyppeteer import launch


async def main():
	browser = await launch()
	page = await browser.newPage()
	await page.goto('https://www.bolsadecaracas.com/resumen-mercado/')
	await page.screenshot({'path': '/home/marcos/Documents/market-api/scripts/bvc-ccs.png'})
	await browser.close()

asyncio.get_event_loop().run_until_complete(main())