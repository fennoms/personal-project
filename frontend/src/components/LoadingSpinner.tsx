import { ColorRing } from "react-loader-spinner";

interface LoadingSpinnerProps {
    width: number;
    height: number;
}

export function LoadingSpinner({ width, height }: LoadingSpinnerProps) {
    return <ColorRing width={width} height={height} />;
}
