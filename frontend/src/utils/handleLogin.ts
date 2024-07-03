"use client";

export const handleLogin = (
    data: any,
    setError: React.Dispatch<React.SetStateAction<string | null>>
) => {
    const formData = new FormData();
    formData.append("username", data.username);
    formData.append("password", data.password);

    fetch("/api/auth/login", {
        method: "POST",
        body: formData,
    })
        .then((res) => {
            if (res.ok) {
                return res.json();
            } else {
                throw new Error("Invalid login credentials. Please try again.");
            }
        })
        .then((data) => {
            localStorage.setItem("token", data.access_token);
            setError(null); // Clear any previous errors on successful login
            // send to /
            window.location.href = "/";
        })
        .catch((error) => {
            setError(error.message); // Set the error message
        });
};
