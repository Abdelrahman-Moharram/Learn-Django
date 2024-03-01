import { useSelector } from 'react-redux'
import { Navigate } from 'react-router-dom'

const PrivateRoutes = ({children}) => {
    let auth = useSelector((state)=>state.auth)
    return(
        auth.IsAuthenticated ? children : <Navigate to="/auth/login"/>
    )
}

export default PrivateRoutes