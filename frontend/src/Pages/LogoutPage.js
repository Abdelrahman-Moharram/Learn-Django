import React from 'react'
import { useDispatch } from 'react-redux'
import { useNavigate } from 'react-router-dom'
import { AuthLogout } from '../state/authSlice'

const LogoutPage = () => {
    const nav =  useNavigate();
    const dispatch = useDispatch()
    dispatch(AuthLogout())
    .unwrap()
    .then(()=>{
        nav("/auth/login")
    }).catch(err=>{
        console.log(err);
    })
  return (
    <div>
      
    </div>
  )
}

export default LogoutPage
