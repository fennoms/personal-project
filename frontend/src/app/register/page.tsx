"use client";

import { buttonVariants } from "@/components/ui/button";
import RegisterForm from "@/forms/RegisterForm";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { useEffect } from "react";
import { useAuth } from "../contexts/authContext";

export default function RegisterPage() {
    const { userId } = useAuth() as { userId: string | null };

    const router = useRouter();

    useEffect(() => {
        if (userId) {
            router.push("/");
        }
    }, [userId]);

    return (
        <div className="flex flex-row h-screen">
            {/* Left side containing logo */}
            <div className="flex flex-col basis-full bg-black"></div>

            {/* Right side containing login form */}
            <div className="flex basis-full">
                <div className="flex justify-center items-center w-full flex-col">
                    <div className="text-center pb-3">
                        <h1 className="font-bold text-xl">Create an account</h1>
                        <h2 className="text-gray-500 text-md">
                            Enter your details below to create an account
                        </h2>
                    </div>
                    <div className="max-w-[300px] w-full">
                        <RegisterForm />
                    </div>
                </div>
            </div>

            {/* Button to redirect to login page, absolute on top right */}
            <div className="absolute right-2 top-2">
                <Link
                    href="/login"
                    className={buttonVariants({ variant: "ghost" })}
                >
                    Log in
                </Link>
            </div>
        </div>
    );
}
