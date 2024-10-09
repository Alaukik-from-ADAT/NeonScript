const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
    res.send('Hello, You have been connected to A.D.A.T. Tech server which is all available in India from any location!');
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
