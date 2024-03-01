import React from 'react'
import { useSelector } from 'react-redux'
const HomePage = () => {

  let auth = useSelector((state)=>state.auth)
  return (
    <div className='mt-4'>
      <p>You are logged in home page {auth.user.username}</p>
    </div>
  )
}

export default HomePage
