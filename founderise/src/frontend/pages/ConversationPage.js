import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ConversationPage = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [conversations, setConversations] = useState([]);

  useEffect(() => {
    // Fetch conversation history
    const fetchConversations = async () => {
      try {
        const response = await axios.get('/api/database/sync'); // Replace with actual endpoint
        setConversations(response.data.conversations || []);
      } catch (error) {
        console.error('Error fetching conversations:', error);
      }
    };

    fetchConversations();
  }, []);

  const handleSendMessage = async () => {
    if (input.trim()) {
      setMessages([...messages, { sender: 'user', text: input }]);
      const userInput = input;
      setInput('');

      try {
        // Send the message to the LLM microservice
        const response = await axios.post('/api/llm/addLLM', { message: userInput });

        if (response.data && response.data.reply) {
          // Update the UI with the LLM's response
          setMessages(prevMessages => [
            ...prevMessages,
            { sender: 'bot', text: response.data.reply }
          ]);
        } else {
          console.error('Invalid response from LLM microservice');
        }
      } catch (error) {
        console.error('Error communicating with LLM microservice:', error);
        setMessages(prevMessages => [
          ...prevMessages,
          { sender: 'bot', text: 'Error: Unable to get a response from the server' }
        ]);
      }
    }
  };

  return (
    <div style={{ padding: '20px', maxWidth: '600px', margin: '0 auto' }}>
      <h1>Conversation</h1>

      <div style={{ marginBottom: '20px' }}>
        <h2>Past Conversations</h2>
        <ul style={{ border: '1px solid #ccc', padding: '10px', listStyle: 'none', maxHeight: '200px', overflowY: 'auto' }}>
          {conversations.map((conversation, index) => (
            <li key={index} style={{ marginBottom: '5px' }}>
              <span>{conversation.title || `Conversation #${index + 1}`}</span>
            </li>
          ))}
        </ul>
      </div>

      <div style={{ border: '1px solid #ccc', padding: '10px', height: '400px', overflowY: 'auto', marginBottom: '10px' }}>
        {messages.map((message, index) => (
          <div
            key={index}
            style={{
              textAlign: message.sender === 'user' ? 'right' : 'left',
              margin: '5px 0',
            }}
          >
            <span
              style={{
                display: 'inline-block',
                padding: '10px',
                borderRadius: '10px',
                backgroundColor: message.sender === 'user' ? '#d1e7dd' : '#f8d7da',
                maxWidth: '70%',
              }}
            >
              {message.text}
            </span>
          </div>
        ))}
      </div>

      <div style={{ display: 'flex' }}>
        <input
          type='text'
          value={input}
          onChange={(e) => setInput(e.target.value)}
          style={{ flex: 1, padding: '10px', fontSize: '16px' }}
          placeholder='Type your message here...' />
        <button
          onClick={handleSendMessage}
          style={{ padding: '10px 20px', marginLeft: '10px', fontSize: '16px' }}
        >
          Send
        </button>
      </div>
    </div>
  );
};

export default ConversationPage;
