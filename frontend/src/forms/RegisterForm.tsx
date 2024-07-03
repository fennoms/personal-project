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

    const [error, setError] = React.useState<string | null>("");

    const onSubmit = (data: any) => {
        handleRegister(data, setError);
    };

    return (
        <FormProvider {...methods}>
            <form
                onSubmit={methods.handleSubmit(onSubmit)}
                className="space-y-4"
            >
                <FormInput
                    name="username"
                    label="Username"
                    placeholder="Enter your username"
                />
                <FormInput
                    name="email"
                    label="Email"
                    placeholder="example@gmail.com"
                />
                <FormInput
                    name="password"
                    label="Password"
                    placeholder="Enter your password"
                    type="password"
                />
                <FormInput
                    name="confirmPassword"
                    label="Confirm Password"
                    placeholder="Confirm your password"
                    type="password"
                />
                <Button type="submit" className="w-full">
                    Submit
                </Button>
            </form>
        </FormProvider>
    );
};

export default RegisterForm;
