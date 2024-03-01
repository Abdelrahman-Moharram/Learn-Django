import { createAsyncThunk, createSlice } from '@reduxjs/toolkit'
import { jwtDecode } from "jwt-decode";

const token = localStorage.getItem("token");


const initialState = {
    user:token?jwtDecode(JSON.parse(token).access):"",
    token:token?JSON.parse(token):"",
    IsAuthenticated: token?true:false,
    IsLoading : false,
    error:null
}
const default_url = "http://127.0.0.1:8000/api/"

export const AuthLogin = createAsyncThunk(
    "Auth/Login",
    async(credintials, thunkAPI) => {
        const {rejectWithValue} = thunkAPI;
        try{
            const response = await fetch(
                default_url+"token",
                {
                    body:JSON.stringify(credintials),
                    method:"POST",
                    headers:{"Content-type":"application/json; charset=UTF-8"}
                })
                if(response.status === 200)
                {
                    const data = await response.json();
                    localStorage.setItem("token", JSON.stringify(data))
                    return data
                }
                else //(response.status === 401)
                    return rejectWithValue(await response.json())


        }
        catch(err){
            return rejectWithValue(err.message)
        }
        
    }
)

export const AuthLogout = createAsyncThunk(
    "Auth/Logout",
    async (_ , thunkAPI)=>{
        const {rejectWithValue} = thunkAPI;
        try{
            localStorage.removeItem("token")
            return true
        }catch(err){
            return rejectWithValue(err.message)
        }
    }
)

const authSlice = createSlice({
    name:"auth",
    initialState,
    reducers:[],
    extraReducers: builder => {

        // LOGIN
        builder.addCase(AuthLogin.pending, (state, action)=>{
            state.IsLoading = true;
            state.IsAuthenticated = false;
        })
        builder.addCase(AuthLogin.fulfilled, (state, action)=>{
            state.IsLoading = false;
            state.IsAuthenticated = true;
            state.token = action.payload
            state.user = jwtDecode(action.payload.access);
        })
        builder.addCase(AuthLogin.rejected, (state, action)=>{
            state.IsLoading = false;
            state.IsAuthenticated = false;
            state.error = action.payload
        })

        // Logout
        builder.addCase(AuthLogout.pending, (state, action)=>{
            state.IsLoading = true;
            state.IsAuthenticated = false;
        })
        builder.addCase(AuthLogout.fulfilled, (state, action)=>{
            state.IsLoading = false;
            state.IsAuthenticated = false;
            state.token = ""
            state.user = {};
        })
        builder.addCase(AuthLogout.rejected, (state, action)=>{
            state.IsLoading = false;
            state.IsAuthenticated = false;
            state.error = action.payload
        })
    }
    
})

export default authSlice.reducer