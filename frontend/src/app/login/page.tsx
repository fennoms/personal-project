"use client";

import { buttonVariants } from "@/components/ui/button";
import LoginForm from "@/forms/LoginForm";
import Link from "next/link";

export default function LoginPage() {
    return (
        <div className="flex flex-row h-screen">
            {/* Left side containing logo */}
            <div className="flex flex-col basis-full bg-black"></div>

            {/* Right side containing login form */}
            <div className="flex basis-full">
                <div className="flex justify-center items-center w-full flex-col">
                    <div className="text-center pb-3">
                        <h1 className="font-bold text-xl">
                            Log in to your account
                        </h1>
                        <h2 className="text-gray-500 text-md">
                            Enter your username and password below to log in
                        </h2>
                    </div>
                    <div className="max-w-[300px] w-full">
                        <LoginForm />
                    </div>
                </div>
            </div>

            {/* Button to redirect to login page, absolute on top right */}
            <div className="absolute right-2 top-2">
                <Link
                    href="/register"
                    className={buttonVariants({ variant: "ghost" })}
                >
                    Register
                </Link>
            </div>
        </div>
    );
}
