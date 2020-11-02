import React, { useContext } from 'react';
import './App.css';

const MyContext = React.createContext(
  { val: 1 }
);

class MyComponet extends React.Component {
  render = () => {
    return (
      <div><p>this is from class component: {this.context.val}</p></div>
    )
  }
}

MyComponet.contextType = MyContext;



function MyComponet2(props: {}) {
  const ctx = useContext(MyContext);
  return (
    <div><p>this is from functional component: {ctx.val}</p></div>
  )
}


function App() {
  return (
    <MyContext.Provider value={{ val: 100 }}>
      <MyComponet />
      <MyComponet2 />
    </MyContext.Provider >
  );
}

export default App;
