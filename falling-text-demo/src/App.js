import FallingText from './FallingText';
import './FallingText.css';

function App() {
  return (
    <div
      className="App"
      style={{
        background: 'transparent',
        minHeight: 'unset',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        width: '100vw',
        height: '180px',
        maxWidth: '1200px',
        margin: '0 auto',
      }}
    >
      <FallingText
        text={`React Bits is a library of animated and interactive React components designed to streamline UI development and simplify your workflow.`}
        highlightWords={["React", "Bits", "animated", "components", "simplify"]}
        highlightClass="highlighted"
        trigger="hover"
        backgroundColor="transparent"
        wireframes={false}
        gravity={0.56}
        fontSize="3.5rem"
        mouseConstraintStiffness={0.9}
      />
    </div>
  );
}

export default App;
