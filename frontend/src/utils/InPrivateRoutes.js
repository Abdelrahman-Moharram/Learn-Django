import { useSelector } from 'react-redux'
import { Navigate } from 'react-router-dom'

const InPrivateRoutes = ({children}) => {
    let auth = useSelector((state)=>state.auth)
    return(
        auth.IsAuthenticated ?  <Navigate to="/"/> : children
    )
}

export default InPrivateRoutes