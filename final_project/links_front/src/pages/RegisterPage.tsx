import {
   Button,
   Modal,
   ModalContent,
   Spinner,
   useDisclosure,
} from '@nextui-org/react';
import { useState } from 'react';
import { useNavigate } from 'react-router';
import useLinkStore from '../store/linksStore';

export const RegisterPage = () => {
   const [username, setUsername] = useState('');
   const [password, setPassword] = useState('');
   const [isLoading, setIsLoading] = useState(false);
   const [error, setError] = useState('');
   const { onClose } = useDisclosure();

   const navigate = useNavigate();

   const { register } = useLinkStore();

   const isButtonDisabled = !username || !password;

   const handleRegister = async () => {
      setIsLoading(true);
      setError('');

      try {
         await register({ username, password });
         setIsLoading(false);
         navigate('/login'); // Redirect to login page after successful registration
      } catch (err: any) {
         setIsLoading(false);
         setError(err.message || 'Ошибка регистрации');
      }
   };

   return (
      <div className="grid justify-center items-center gap-4 mt-10">
         <div className="grid justify-center items-center">
            <h2 className="text-3xl font-semibold text-center">Регистрация</h2>
            <p className="font-semibold text-center text-sm text-gray-500 mt-1">
               Управление ссылками!
            </p>
         </div>
         <div className="grid justify-center items-center">
            <p className="font-semibold text-start text-sm text-gray-500">
               Имя пользователя
            </p>
            <input
               className="grid border rounded-xl p-2 min-w-72 mt-1"
               type="text"
               value={username}
               onChange={(e) => setUsername(e.target.value)}
               placeholder="username"
            />
         </div>
         <div className="grid justify-center items-center">
            <p className="font-semibold text-start text-sm text-gray-500">
               Пароль
            </p>
            <input
               className="grid border rounded-xl p-2 min-w-72 mt-1"
               type="password"
               value={password}
               onChange={(e) => setPassword(e.target.value)}
               placeholder="password"
            />
         </div>
         <div className="grid justify-center items-center">
            <Button
               color="danger"
               variant="shadow"
               className="min-w-72 font-semibold"
               isDisabled={isButtonDisabled}
               onPress={handleRegister}
            >
               Регистрация
            </Button>
         </div>
         <div className="flex gap-4 justify-center">
            <p className="font-semibold text-sm text-gray-500">
               У Вас уже есть аккаунт?
            </p>
            <a className="font-semibold text-sm text-blue-700" href="/login">
               Войти
            </a>
         </div>
         <Modal
            isOpen={isLoading || error !== ''}
            onClose={() => {
               setIsLoading(false);
               setError('');
               onClose();
            }}
         >
            <ModalContent>
               <div className="flex justify-center items-center gap-3 p-5">
                  {isLoading ? (
                     <>
                        <h3>Загрузка...</h3>
                        <Spinner />
                     </>
                  ) : (
                     <h3>{error}</h3>
                  )}
               </div>
            </ModalContent>
         </Modal>
      </div>
   );
};

export default RegisterPage;
