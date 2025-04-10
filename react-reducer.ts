// https://legacy.reactjs.org/docs/hooks-reference.html#usereducer
//
// useReducer is usually preferable to useState when you have 
// complex state logic that involves multiple sub-values or 
// when the next state depends on the previous one.
// useReducer also lets you optimize performance for components 
// that trigger deep updates because you can pass dispatch down 
// instead of callbacks.
//
// For dispatch data, context may still be more appropriate.

import { useReducer } from "react";

const initialState = {
    rowData: [],
    columnDefs: [],
    loading: true,
    open: false,
    statusMessage: "",
    dataMessage: "",
    dataId: null,
};

const reducer = (state, action) => {
    switch (action.type) {
        case "SET_ROW_DATA":
            return { ...state, rowData: action.payload };
        case "SET_COLUMN_DEFS":
            return { ...state, columnDefs: action.payload };
        case "SET_LOADING":
            return { ...state, loading: action.payload };
        case "SET_OPEN":
            return { ...state, open: action.payload };
        case "STATUS_MESSAGE":
            return { ...state, statusMessage: action.payload };
        case "SET_DATA_DETAILS":
            return {
                ...state,
                dataName: action.payload.dataName,
                dataId: action.payload.dataId,
            };
        default:
            return state;
    }
};

const [state, dispatch] = useReducer(reducer, initialState);

// Placeholder
const getData = () => Promise.resolve({ data: [] });

const fetchData = async () => {
    try {
        const data = await getData();
        dispatch({ type: "SET_ROW_DATA", payload: data.data });
    } catch (error) {
        console.error(error);
    } finally {
        dispatch({ type: "SET_LOADING", payload: false });
    }
};