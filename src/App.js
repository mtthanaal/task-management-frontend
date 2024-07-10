import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { Provider } from 'react-redux';
import { store } from './redux/store';
import Login from './components/Login';
import Dashboard from './components/Dashboard';
import TaskForm from './components/TaskForm';
import TaskItem from './components/TaskItem';

const App = () => {
  return (
    <Provider store={store}>
      <Router>
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/taskform" element={<TaskForm/>} />
          <Route path="/taskitem" element={<TaskItem/>} />
        </Routes>
      </Router>
    </Provider>
  );
};

export default App;
