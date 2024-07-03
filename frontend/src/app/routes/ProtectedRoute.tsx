import { useRouter } from "next/navigation";
import { ReactNode } from "react";
import { useAuth } from "../contexts/authContext";

interface ProtectedRouteProps {
    children: ReactNode;
}

const ProtectedRoute: React.FC<ProtectedRouteProps> = ({ children }) => {
    const { userId } = useAuth() as { userId: string | null };
    const router = useRouter();

    if (!userId) {
        router.push("/login");
        return null;
    }

    return <>{children}</>;
};

export default ProtectedRoute;
