'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class Ayam extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // define association here
    }
  }
  Ayam.init({
    umur: DataTypes.INTEGER,
    berat: DataTypes.FLOAT,
    jenis: DataTypes.STRING
  }, {
    sequelize,
    modelName: 'Ayam',
  });
  return Ayam;
};