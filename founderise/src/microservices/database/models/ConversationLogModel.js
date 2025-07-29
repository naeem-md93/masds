'use strict';

const { DataTypes, Model } = require('sequelize');
const sequelize = require('../config/database'); // Adjust path if config file differs

class ConversationLog extends Model {}

ConversationLog.init(
  {
    id: {
      type: DataTypes.INTEGER,
      autoIncrement: true,
      primaryKey: true,
    },
    conversationId: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    sender: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    message: {
      type: DataTypes.TEXT,
      allowNull: false,
    },
    createdAt: {
      type: DataTypes.DATE,
      defaultValue: DataTypes.NOW,
    },
    updatedAt: {
      type: DataTypes.DATE,
      defaultValue: DataTypes.NOW,
    },
  },
  {
    sequelize,
    modelName: 'ConversationLog',
    tableName: 'conversation_logs',
    timestamps: true,
  }
);

module.exports = ConversationLog;
