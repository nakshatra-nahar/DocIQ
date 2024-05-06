# dociq react widget


This widget will allow you to embed a dociq assistant in your React app.

## Installation

```bash
npm install  dociq
```

## Usage

```javascript
    import { dociqWidget } from "dociq";

    const App = () => {
      return <dociqWidget />;
    };
```

To link the widget to your api and your documents you can pass parameters to the <dociqWidget /> component.

```javascript
    import { dociqWidget } from "dociq";

    const App = () => {
      return <dociqWidget 
             apiHost = 'http://localhost:7001',
             selectDocs = 'default', 
             apiKey = '',
             avatar = 'https://d3dg1063dc54p9.cloudfront.net/cute-dociq.png',
             title = 'Get AI assistance',
             description = 'dociq\'s AI Chatbot is here to help',
             heroTitle = 'Welcome to dociq !',
             heroDescription='This chatbot is built with dociq and utilises GenAI, please review important information using sources.'
             />;
    };
```


## Our github

[dociq](https://github.com/arc53/dociq)

You can find the source code in the extensions/react-widget folder.

