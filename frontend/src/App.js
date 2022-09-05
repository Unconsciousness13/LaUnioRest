import './App.css';
import './components/GymnastsList'
import GymnastsList from './components/GymnastsList';
import TrainersList from './components/TrainersList';
import Header from './components/Header';

function App() {
  return (
    <div className="App">
      <Header />
      <h1>Hello Django React</h1>
      <GymnastsList />
      <TrainersList/>
    </div>
  );
}

export default App;
