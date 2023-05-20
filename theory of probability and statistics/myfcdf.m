
function p = myfcdf (x, m, k)

    if (k <= x * m)
        xx = k / (k + x * m);
        p = romberg(xx, m/2, k/2, 0.000001,1);
    else
        num = m * x;
        xx = num / (num + k);
        p = romberg(xx, m/2, k/2, 0.000001,0);
    end

endfunction
