export const handleRegister = (
    data: any,
    setError: React.Dispatch<React.SetStateAction<string | null>>
) => {
    fetch("/api/auth/register", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            email: data.email,
            username: data.username,
            password: data.password,
            confirm: data.confirmPassword,
        }),
    })
        .then((res) => {
            if (res.ok) {
                return res.json();
            } else {
                throw new Error("Something went wrong");
            }
        })
        .then((data) => {
            localStorage.setItem("token", data.access_token);
            setError(null);
            window.location.href = "/";
        })
        .catch((error) => {
            setError(error.message);
        });
};
