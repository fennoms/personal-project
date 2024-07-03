"use client";

import {
    createContext,
    ReactNode,
    useContext,
    useEffect,
    useState,
} from "react";

interface AuthContextProps {
    userId: string | null;
    setUserId: (userId: string | null) => void;
    username: string | null;
    setUsername: (username: string | null) => void;
}

const AuthContext = createContext<AuthContextProps | undefined>(undefined);

export const AuthContextProvider = ({ children }: { children: ReactNode }) => {
    const [userId, setUserId] = useState<string | null>(null);
    const [username, setUsername] = useState<string | null>(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const token = localStorage.getItem("token");
        if (!token) {
            setUserId(null);
            setUsername(null);
            setLoading(false);
            return;
        }

        fetch("/api/auth/verify", {
            headers: {
                Authorization: `Bearer ${token}`,
            },
        })
            .then((res) => {
                if (res.ok) {
                    return res.json();
                } else {
                    setUserId(null);
                    setUsername(null);
                    setLoading(false);
                    throw new Error("Something went wrong");
                }
            })
            .then((data) => {
                setUserId(data.id);
                setUsername(data.username);
                setLoading(false);
            })
            .catch((error) => {
                console.error("Error:", error);
            });
    }, []);

    return (
        !loading && (
            <AuthContext.Provider
                value={{ userId, setUserId, username, setUsername }}
            >
                {children}
            </AuthContext.Provider>
        )
    );
};

export const useAuth = () => {
    return useContext(AuthContext);
};
