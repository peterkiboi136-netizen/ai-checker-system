const handleLogin = async () => {
  try {
    const res = await api.post("/auth/login", {
      email,
      password,
    });

    localStorage.setItem("token", res.data.access_token);

    navigate("/dashboard");
  } catch (err) {
    console.log(err);
    alert("Login failed");
  }
};

import React, { useState } from "react";
import axios from "axios";

function Login() {

    const [email, setEmail] = useState("");

    const [password, setPassword] = useState("");

    const handleLogin = async () => {

        try {

            const response = await axios.post(
                "http://127.0.0.1:8000/auth/login",
                null,
                {
                    params: {
                        email,
                        password
                    }
                }
            );

            localStorage.setItem(
                "token",
                response.data.access_token
            );

            alert("Login successful");

        } catch (error) {

            alert("Login failed");
        }
    };

    return (

        <div
            style={{
                padding: 40
            }}
        >

            <h1>Login</h1>

            <input
                placeholder="Email"
                value={email}
                onChange={(e) =>
                    setEmail(e.target.value)
                }
            />

            <br /><br />

            <input
                type="password"
                placeholder="Password"
                value={password}
                onChange={(e) =>
                    setPassword(e.target.value)
                }
            />

            <br /><br />

            <button onClick={handleLogin}>
                Login
            </button>

        </div>
    );
}

export default Login;