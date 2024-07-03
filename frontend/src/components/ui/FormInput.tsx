"use client";

// FormInput.tsx
import React from "react";
import { useFormContext } from "react-hook-form";
import {
    FormField,
    FormItem,
    FormLabel,
    FormControl,
    FormDescription,
    FormMessage,
} from "@/components/ui/form";
import { Input } from "@/components/ui/input";

interface FormInputProps {
    name: string;
    label: string;
    placeholder: string;
    description?: string;
    type?: string;
}

const FormInput: React.FC<FormInputProps> = ({
    name,
    label,
    placeholder,
    description,
    type,
}) => {
    const { control } = useFormContext(); // Ensure you are within the provider scope of react-hook-form

    return (
        <FormField
            control={control}
            name={name}
            render={({ field }) => (
                <FormItem>
                    <FormLabel>{label}</FormLabel>
                    <FormControl>
                        <Input
                            type={type}
                            placeholder={placeholder}
                            {...field}
                            className="w-full"
                        />
                    </FormControl>
                    <FormDescription>{description}</FormDescription>
                    <FormMessage />
                </FormItem>
            )}
        />
    );
};

export default FormInput;
