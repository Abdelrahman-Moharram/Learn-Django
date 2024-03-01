import React, {useState} from 'react'
import { Link, useNavigate } from 'react-router-dom'
import {useDispatch} from 'react-redux'
import { AuthLogin } from '../state/authSlice'

const LoginPage = () => {
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")

    const [usernameValidation, setUsernameValidation] = useState("")
    const [passwordValidation, setPasswordValidation] = useState("")
    
    const [err, setErr] = useState(null)
    const nav =  useNavigate();
    const dispatch = useDispatch()

    const HandleSubmit = (e)=>{
        e.preventDefault()
        
        if(!username)
            setUsernameValidation("Username shouldn't be Empty or null")
        if(!password)
            setPasswordValidation("Password shouldn't be Empty or null")

        if(!username || !password)
            return 

        dispatch(AuthLogin({username, password}))
            .unwrap()
            .then(()=>{
                nav("/")
            }).catch(err=>{
                setPassword("")
                setErr(err['detail'])
            })
    }
  return (
    <div className='container p-5'>
        <form className={usernameValidation? 'w-75 mx-auto bg-light mt-5 p-5 default-shadow was-validated':"w-75 mx-auto bg-light mt-5 p-5 default-shadow"} noValidate style={{boxShadow:"0px 0px 10px #000", borderRadius:"10px"}} method='post' onSubmit={HandleSubmit}>
            {
                err?
                    <div className="text-danger text-center fw-bold my-4">{err}</div>:
                ""
            }
            <div data-mdb-input-init className={"mb-4 form-outline" }>
                <input type="text" id="UserName" value={username} onChange={(e)=>setUsername(e.target.value)} className="form-control" required />
                <label className="form-label" htmlFor="UserName">User Name</label>
                {
                    usernameValidation?
                    <div className="is-invalid">{usernameValidation}</div>
                    :""
                }
            </div>
            
            
            
            <div data-mdb-input-init className="form-outline mb-4">
                <input type="password" id="form1Example2" value={password} onChange={(e)=>setPassword(e.target.value)} className="form-control" required />
                <label className="form-label" htmlFor="form1Example2">Password</label>
                {
                    usernameValidation ?
                    <div className="is-invalid">{passwordValidation}</div>
                    :""
                    // <div className="is-valid">Looks Good</div>
                }
            </div>

            
            <div className="row mb-4">
                <Link to="#!" className='text-center'>Forgot password?</Link>
            </div>

            <button data-mdb-ripple-init type="submit" className="btn btn-primary btn-block">Sign in</button>
        </form>
    </div>
  )
}

export default LoginPage