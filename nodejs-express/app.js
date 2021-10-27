const express = require('express')
const app = express()
const port = 8080

app.get('/', (req, res) => {
  console.log(`${req.method} ${req.host} ${req.originalUrl}`)
  res.send('Hello World!')
})

app.listen(port, '0.0.0.0', () => {
  console.log(`Example app listening at http://0.0.0.0:${port}`)
})
