import './App.css';
import { LikeButton, DislikeButton } from './Buttons.js';
import 'bootstrap/dist/css/bootstrap.min.css';


const Content = class {
  constructor(username, text) {
    this.username = username;
    this.text = text;
  }
}

const content = new Content("Username", "Some quick example text to build on the card title and make up the bulk of the card's content")

function App() {
  return (
    <div class="container">
      <div class="card">
        <div class="card-body text-center">
          <h5 class="card-title">{content.username}</h5>
          <p class="card-text">{content.text}</p>
          <LikeButton />
          <DislikeButton />
        </div>
      </div>
    </div>
  );
}

export default App;
