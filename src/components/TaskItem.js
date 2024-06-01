import React from 'react';
import { useDispatch } from 'react-redux';
import { updateTask, deleteTask } from '../redux/tasksSlice';

const TaskItem = ({ task }) => {
  const dispatch = useDispatch();

  const handleStatusChange = (e) => {
    dispatch(updateTask({ ...task, status: e.target.value }));
  };

  const handleDelete = () => {
    dispatch(deleteTask(task.id));
  };

  return (
    <div>
      <h4>{task.title}</h4>
      <p>{task.description}</p>
      <p>Assignee: {task.assignee}</p>
      <select value={task.status} onChange={handleStatusChange}>
        <option value="pending">Pending</option>
        <option value="in progress">In Progress</option>
        <option value="completed">Completed</option>
      </select>
      <button onClick={handleDelete}>Delete</button>
    </div>
  );
};

export default TaskItem;
