import React from 'react';
import { useForm, FormProvider } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { Button } from '@/components/ui/button';
import FormInput from '@/components/ui/FormInput';
import { handleLogin } from '@/utils/handleLogin';
import { loginFormSchema } from '@/utils/loginFormSchema';


const LoginForm: React.FC = () => {
    const methods = useForm({
        resolver: zodResolver(loginFormSchema),
        defaultValues: {
            username: '',
            password: '',
        },
    });



  return (
    <FormProvider {...methods}>
      <form onSubmit={methods.handleSubmit(handleLogin)} className="space-y-8">
        <FormInput
          name="username"
          label="Username"
          placeholder="Enter your username"
          description="This is your public display name."
        />
        <FormInput
          name="password"
          label="Password"
          placeholder="Enter your password"
          description="This is your password."
          type="password"
        />
        <Button type="submit">Submit</Button>
      </form>
    </FormProvider>
  );
};

export default LoginForm;
