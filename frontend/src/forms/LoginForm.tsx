import React from "react";
import { useForm, FormProvider } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { Button } from "@/components/ui/button";
import FormInput from "@/components/ui/FormInput";
import { handleLogin } from "@/utils/handleLogin";
import { loginFormSchema } from "@/utils/loginFormSchema";

const LoginForm: React.FC = () => {
    const methods = useForm({
        resolver: zodResolver(loginFormSchema),
        defaultValues: {
            username: "",
            password: "",
        },
    });

    const [error, setError] = React.useState<string | null>();

    const onSubmit = (data: any) => {
        handleLogin(data, setError);
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
                    name="password"
                    label="Password"
                    placeholder="Enter your password"
                    type="password"
                />
                <Button type="submit" className="w-full">
                    Submit
                </Button>
                {error && <p className="text-red-500 text-center">{error}</p>}
            </form>
        </FormProvider>
    );
};

export default LoginForm;
