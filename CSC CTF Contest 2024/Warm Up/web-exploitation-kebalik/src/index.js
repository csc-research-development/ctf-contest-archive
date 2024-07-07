import express from 'express'
import cookieParser from 'cookie-parser'
import sanitizeHtml from 'sanitize-html'

const app = express()
const port = 5005

app.use(express.static('public'))
app.use(cookieParser())

app.use((req, res, next) => {
	const { rotate } = req.cookies
	req.rotate = rotate
	if (!rotate) {
		req.rotate = '180'
		res.cookie('rotate', req.rotate, {
			path: '/',
			httpOnly: true,
		})
	}
	next()
})

const disableDevToolsShortcuts = `
	document.addEventListener('contextmenu', (event) => {
		event.preventDefault();
	});

	document.addEventListener('keydown', (event) => {
		if ((event.ctrlKey && event.shiftKey && ['c', 'i', 'j', 'k'].includes(event.key.toLowerCase())) || (event.key === 'F12')) {
			event.preventDefault();
		}
	});
`

app.get('/', (req, res) => {
	if (
		(req.rotate == 0 && req.rotate.length == 1) ||
		req.rotate.startsWith('00')
	) {
		return res.send(`
			<!DOCTYPE html>
			<html lang="en">
				<head>
					<meta charset="UTF-8" />
					<meta name="viewport" content="width=device-width, initial-scale=1.0" />
					<title>hehe</title>
					<style>
						code {
							font-family: Consolas, Monaco, 'Andale Mono', 'Ubuntu Mono', monospace;
						}
					</style>
				</head>
				<body>
					<p>wadu kok bocor 💀</p>
				<pre>
if ((req.rotate == 0 && req.rotate.length == 1) || req.rotate.startsWith('00')) {
	return res.send(\`tidak semudah itu hehe, tapi dikit lagi ngab 🗿 coba pikirin gmn caranya naro 0 tapi bukan 0 tapi valid sebagai 0 🗿\`)
}
<br />
if (req.rotate == 0) {
	// 🚩
}
					</pre>
					<script>${disableDevToolsShortcuts}</script>
				</body>
			</html>
		`)
	}
	if (req.rotate == 0) {
		return res.send(`
			<!DOCTYPE html>
			<html lang="en">
				<head>
					<meta charset="UTF-8" />
					<meta name="viewport" content="width=device-width, initial-scale=1.0" />
					<title>udh ga kebalik</title>
				</head>
				<body style="transform: rotate(${+sanitizeHtml(req.rotate)}deg)">
					<img id="img" src="/happy.jpg" style="width: 250px; height: 250px; object-fit: cover" />
					<h1>gege udh ga kebalik</h1>
					<p id="flag">ini flagnya: <span>CSC%7Bku3%5Fk3r1nG%5Fw3bS1tE%5Fm3N4r1K%5FjUg4%5Fehe%7D<span></p>
					<script>
						const flag = document.getElementById('flag')
						const img = document.getElementById('img')

						flag.querySelector('span').innerHTML = decodeURI(flag.querySelector('span').innerHTML)
						
						setTimeout(() => {
							flag.innerHTML = 'yah lama lu 🗿'
							img.src = "/sad.jpg"
						}, 600)
					
						${disableDevToolsShortcuts}
					</script>
				</body>
			</html>	
		`)
	}
	res.send(`
		<!DOCTYPE html>
		<html lang="en">
			<head>
				<meta charset="UTF-8" />
				<meta name="viewport" content="width=device-width, initial-scale=1.0" />
				<title>kebalik</title>
				<style>
					body {
						margin: 0;
						padding: 0;
						font-family: sans-serif;
					}
				</style>
			</head>
			<body style="transform: rotate(${+sanitizeHtml(
				req.rotate
			)}deg); text-align: center; display: grid; place-items: center; min-height: 100vh">
				<div>
					<h1>aduh ini napa kebalik cuk 💀🗿</h1>
					<p>tolongg ngab, entar gw kasih flagnya</p>
					<img src="/patrick.jpg" width="200" />
				</div>
				<script>
					${disableDevToolsShortcuts}
				</script>
			</body>
		</html>																		
	`)
})

app.listen(port, () => {
	console.log(`Server listening on http://localhost:${port}`)
})
