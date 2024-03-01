import React from 'react';
import './index.css';
import reportWebVitals from './reportWebVitals';
import HomePage from './Pages/HomePage';
import LoginPage from './Pages/LoginPage';
import AboutPage from './Pages/AboutPage'
import { createRoot } from "react-dom/client";
import store from './state';
import {
  createBrowserRouter,
  RouterProvider,

} from "react-router-dom";
import { Provider } from "react-redux";
import Layout from './Pages/Shared/Layout';
import PrivateRoutes from './utils/PrivateRoutes';
import InPrivateRoutes from './utils/InPrivateRoutes';
import LogoutPage from './Pages/LogoutPage';


const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout />,
    
    children:[
      {
        index:true,
        element: 
        <PrivateRoutes>
          <HomePage />
        </PrivateRoutes>
      },
      {
        path:"about",
        element:
        <PrivateRoutes>
          <AboutPage />
        </PrivateRoutes>
      },
      
    ]
  },
  {
    path: "auth",
    children:[
      {
        path:"login",
        element: 
        <InPrivateRoutes>
          <LoginPage />,
        </InPrivateRoutes>
      },
      {
        path:"logout",
        element: 
        <PrivateRoutes>
          <LogoutPage />
        </PrivateRoutes>
        ,
      },

    ]
  },
]);

createRoot(document.getElementById("root")).render(
  <Provider  store={store}>
    <RouterProvider router={router} />
  </Provider>
);
// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
