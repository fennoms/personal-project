"use client";

import { useRouter } from "next/navigation";
import { ReactNode, use, useEffect } from "react";
import { useAuth } from "../contexts/authContext";

interface ProtectedRouteProps {
    children: ReactNode;
}

const ProtectedRoute: React.FC<ProtectedRouteProps> = ({ children }) => {
    const { userId } = useAuth() as { userId: string | null };
    const router = useRouter();

    useEffect(() => {
        if (!userId) {
            router.push("/login");
        }
    }, [userId]);

    return <>{children}</>;
};

export default ProtectedRoute;
