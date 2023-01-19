import './App.css';
import { LikeButton, DislikeButton } from './Buttons.js';
import 'bootstrap/dist/css/bootstrap.min.css';


const Content = class {
  constructor(username, text) {
    this.username = username;
    this.text = text;
  }
}

function App() {
  return (
    <div class="container">
      <div class="card">
        <div class="card-body text-center">
          <h5 class="card-title">Username</h5>
          <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's
            content.</p>
          <LikeButton />
          <DislikeButton />
        </div>
      </div>
    </div>
  );
}

export default App;
