const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const { Sequelize, DataTypes } = require('sequelize');

const app = express();
const port = process.env.PORT || 3000;

app.use(cors());
app.use(bodyParser.json());

const sequelize = new Sequelize({
  dialect: 'sqlite',
  storage: './database.development.sqlite',
});

const Ayam = require('./models/ayam')(sequelize, DataTypes);

const asyncMiddleware = (fn) => (req, res, next) => {
  Promise.resolve(fn(req, res, next)).catch(next);
};

app.get('/api/ayam', asyncMiddleware(async (req, res) => {
  const ayamList = await Ayam.findAll();
  res.json(ayamList);
}));

app.get('/api/ayam/:id', asyncMiddleware(async (req, res) => {
  const { id } = req.params;
  const ayam = await Ayam.findByPk(id);

  if (!ayam) {
    return res.status(404).json({ error: 'Ayam not found.' });
  }

  res.json(ayam);
}));

app.post('/api/ayam', asyncMiddleware(async (req, res) => {
  const { umur, beratAyam, jenisAyam } = req.body;

  if (!umur || !beratAyam || !jenisAyam) {
    return res.status(400).json({ error: 'Umur, Berat Ayam, dan Jenis Ayam harus diisi.' });
  }

  const newAyam = await Ayam.create({ umur, beratAyam, jenisAyam });
  console.log('New Ayam created:', newAyam.toJSON());

  res.json({ message: 'Ayam added successfully', newAyam });
}));

app.put('/api/ayam/:id', asyncMiddleware(async (req, res) => {
  const { id } = req.params;
  const { umur, beratAyam, jenisAyam } = req.body;

  const ayam = await Ayam.findByPk(id);

  if (!ayam) {
    return res.status(404).json({ error: 'Ayam not found.' });
  }

  ayam.umur = umur;
  ayam.beratAyam = beratAyam;
  ayam.jenisAyam = jenisAyam;

  await ayam.save();

  res.json({ message: 'Ayam updated successfully', ayam });
}));

app.delete('/api/ayam/:id', asyncMiddleware(async (req, res) => {
  const { id } = req.params;

  const ayam = await Ayam.findByPk(id);

  if (!ayam) {
    return res.status(404).json({ error: 'Ayam not found.' });
  }

  await ayam.destroy();

  res.json({ message: 'Ayam deleted successfully' });
}));

app.listen(port, async () => {
  console.log(`Server is running on port ${port}`);

  try {
    await sequelize.authenticate();
    console.log('Database connection has been established successfully.');
  } catch (error) {
    console.error('Unable to connect to the database:', error.message);
  }
});
