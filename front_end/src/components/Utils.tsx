import { Alert } from "@mui/material";
import Lottie from "lottie-react";
import { OhlcData } from "./DataManagement";


interface NoDataAnimationProps {
    data: OhlcData,
    chartHeight: number
}

interface NoDataProps {
    dataType: string,
    marginTop: number
}

export function NoDataAnimation(props: NoDataAnimationProps) {
    return (
        <div>
            <Lottie animationData={props.data} style={{ height: props.chartHeight }} />
        </div>
    );
}

export function NoData(props: NoDataProps) {
    return (
        <Alert sx={{ display: "flex", justifyContent: "center", marginTop: props.marginTop }} severity="error">
            {`Failed to fetch ${props.dataType} data`}
        </Alert>
    )
}