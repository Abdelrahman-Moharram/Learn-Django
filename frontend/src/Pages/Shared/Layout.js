import React from 'react'
import NavBar from '../../Components/Headers/NavBar'
import { Outlet } from 'react-router-dom'

const Layout = () => {
  return (
    <div>
        <NavBar />
        <div className='my-4'></div>
        <Outlet />
    </div>
  )
}

export default Layout