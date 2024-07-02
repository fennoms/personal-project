export const handleLogin = (data: any) => {
    const formData = new FormData();
    formData.append('username', data.username);
    formData.append('password', data.password);

    fetch('/api/auth/login', {
        method: 'POST',
        body: formData,
    }).then((res) => {
        if (res.ok) {
            return res.json();
        } else {
            throw new Error('Something went wrong');
        }
    }).then((data) => {
        localStorage.setItem('token', data.access_token);
    }).catch((error) => {
        console.error('Error:', error);
    });
};
