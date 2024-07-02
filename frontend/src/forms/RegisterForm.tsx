import React from "react";
import { useForm, FormProvider } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { registerFormSchema } from "@/utils/registerFormSchema";
import { Button } from "@/components/ui/button";
import FormInput from "@/components/ui/FormInput";
import { handleRegister } from "@/utils/handleRegister";

const RegisterForm: React.FC = () => {
    const methods = useForm({
        resolver: zodResolver(registerFormSchema),
        defaultValues: {
            email: "",
            username: "",
            password: "",
            confirmPassword: "",
        },
    });

    return (
        <FormProvider {...methods}>
            <form
                onSubmit={methods.handleSubmit(handleRegister)}
                className="space-y-8"
            >
                <FormInput
                    name="username"
                    label="Username"
                    placeholder="Enter your username"
                    description="This is your public display name."
                />
                <FormInput
                    name="email"
                    label="Email"
                    placeholder="example@gmail.com"
                    description="Enter your email address."
                />
                <FormInput
                    name="password"
                    label="Password"
                    placeholder="Enter your password"
                    description="Choose a strong password."
                    type="password"
                />
                <FormInput
                    name="confirmPassword"
                    label="Confirm Password"
                    placeholder="Confirm your password"
                    description="Confirm your password."
                    type="password"
                />
                <Button type="submit">Submit</Button>
            </form>
        </FormProvider>
    );
};

export default RegisterForm;
