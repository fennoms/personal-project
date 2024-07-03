"use client";

import { useAuth } from "./contexts/authContext";

export default function Home() {
    const { userId } = useAuth() as { userId: string | null };

    return (
        <>
            {userId ? (
                <>
                    <h1>Home</h1>
                    <p>Welcome back, user {userId}!</p>
                </>
            ) : (
                <>
                    <h1>Home</h1>
                    <p>Welcome to the home page!</p>
                </>
            )}
        </>
    );
}
