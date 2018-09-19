CREATE DATABASE IF NOT EXISTS mydb;

use mydb;

CREATE TABLE IF NOT EXISTS answers (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  question VARCHAR(300) NOT NULL,
  answer VARCHAR(300) NOT NULL);
  
INSERT INTO answers (question, answer) VALUES
  ('Does he have any academic degree?', 'Yes. He recieved his bachelor degree in Computer Science from the University of Tehran in 2018'),
  ('Where did he recieved his bachelor degree?', 'University of Tehran'),
  ('When did he recieved his bachelor degree?','July 2018'),
  ('Tell me about his fields of intrest', 'His main intrest is developing chatbots using neural networks and he is hoping to take it further someday.'),
  ('Does he have any work experience?', 'Yes. He was employed as machine learning engineer in January 2018 and has been working there since. He also co-founded his own company in 2015 which is active in the field of artificial intelligence.'),
  ('Where does he live?', 'Currently, he is living in Tehran. He will be relocated to Pisa ASAP.');
