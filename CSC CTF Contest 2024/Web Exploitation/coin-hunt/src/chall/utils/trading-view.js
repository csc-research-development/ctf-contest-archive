import TradingView from '@mathieuc/tradingview'
import { symbol } from '../index.js'

if (!global.client) {
	global.client = new TradingView.Client()
}

const client = global.client

export function getLastPrice() {
	const chart = new client.Session.Chart()

	chart.setMarket(symbol, {
		timeframe: '1M',
	})

	return new Promise((resolve) => {
		chart.onUpdate(() => {
			if (!chart.periods[0]) return
			resolve(chart.periods[0].close)
			chart.delete()
		})
	})
}
