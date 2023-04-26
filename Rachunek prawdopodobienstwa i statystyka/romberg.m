function result = romberg(x, a, b, eps,flag)
  % x - argument funkcji
  % a, b - parametry funkcji
  % eps - dokładność obliczeń
  % flag - wartość logiczna określająca, czy obliczenia mają być prowadzone dla dolnej granicy całkowania (flag = 0) czy górnej (flag = 1)

  % Definicja funkcji podcałkowej
  f = @(t) t^(a-1) * (1-t)^(b-1);

  % Definicja funkcji beta
  beta = gamma(a) * gamma(b) / gamma(a+b);

  % Definicja macierzy Romberga
  R = zeros(20,20);

  % Wyliczenie pierwszego przybliżenia całki
  if flag == 0
    R(1,1) = (f(0) + f(x)) * x / 2;
  else
    R(1,1) = (f(1-x) + f(1)) * (1-x) / 2;
  endif

  % Generowanie kolejnych przybliżeń
  for j = 2:20
    if flag == 0
      h = (x-0) / 2^(j-1);
      sum = 0;
      for k = 1:2^(j-2)
        sum += f(0 + (2*k-1)*h);
      endfor
      R(j,1) = 0.5*R(j-1,1) + sum*h;
    else
      h = (1-x) / 2^(j-1);
      sum = 0;
      for k = 1:2^(j-2)
        sum += f(1 - (2*k-1)*h - x);
      endfor
      R(j,1) = 0.5*R(j-1,1) + sum*h;
    endif
    for i = 2:j
      R(j,i) = (4^(i-1) * R(j,i-1) - R(j-1,i-1)) / (4^(i-1) - 1);
    endfor
    % Sprawdzenie warunku stopu
    if abs(R(j-1,j-1) - R(j,j)) < eps
      result = R(j,j) / beta;
      return
    endif
  endfor

  % Zwrócenie wyniku
  result = R(20,20) / beta;
endfunction

