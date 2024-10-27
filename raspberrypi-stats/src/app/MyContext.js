// MyContext.js
"use client";

import { createContext, useContext, useState } from 'react';

// Crea el contexto
const MyContext = createContext();

// Proveedor del contexto
export const MyProvider = ({ children }) => {
    const [state, setState] = useState({ data: null });

    return (
        <MyContext.Provider value={{ state, setState }}>
            {children}
        </MyContext.Provider>
    );
};

// Hook para usar el contexto
export const useMyContext = () => {
    return useContext(MyContext);
};
