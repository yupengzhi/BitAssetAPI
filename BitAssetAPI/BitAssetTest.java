package com.example.jmeter.demo;

import com.example.jmeter.util.EncryptDigestUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.springframework.web.client.RestTemplate;

import java.util.HashMap;
import java.util.LinkedHashMap;

/**
 * 描   述: 关于签名demo代码，有关签名相关demo
 *
 * @author caibangchao
 * @version [版本号, 2018/8/1]
 * @see [相关类/方法]
 * 创建日期: 2018/8/1
 */
@Component
public class BitAssetTest {


    @Autowired
    private RestTemplate restTemplate;

    private String url = "http://api.bitasset.com";


    /**
     * 获取账户资金
     * paramMap中的key除了apiSign之外，要按升序排列 如apiAccessKey在apiTimeStamp前面
     * 
     * @return
     */
    public String getAccount() {
        HashMap<String, Object> paramMap = new LinkedHashMap<String, Object>();
        String apiTimeStamp = String.valueOf(System.currentTimeMillis());
        paramMap.put("apiAccessKey", "你的apiAccessKey");
        paramMap.put("apiTimeStamp", apiTimeStamp);
        String apiSign = signUp(paramMap, "你的apiSecretKey");
        paramMap.put("apiSign", apiSign);
        String result = restTemplate.getForObject(url + "/v1/cash/accounts/balance?apiAccessKey={apiAccessKey}"
                + "&apiTimeStamp={apiTimeStamp}" + "&apiSign={apiSign}", String.class, paramMap);

        return result;
    }

    public static String signUp(Map<String, Object> map, String secretKey) {
        String params = signUpParam(map);
        String secret = digest(secretKey);
        return HMACSHA256(params, secret);
    }

    public static String signUpParam(Map<String, Object> paramMap) {
        StringBuilder sb = new StringBuilder();
        for (String key : paramMap.keySet()) {
            sb.append(key).append("=").append(paramMap.get(key)).append("&");
        }
        return sb.substring(0, sb.length() - 1);
    }

    /**
     * SHA加密
     */
    public static String digest(String valueStr) {
        valueStr = valueStr.trim();
        byte value[];
        try {
            value = valueStr.getBytes("UTF-8");
        } catch (UnsupportedEncodingException e) {
            throw new RuntimeException(e);
        }
        MessageDigest md = null;
        try {
            md = MessageDigest.getInstance("SHA");
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException(e);
        }
        return toHex(md.digest(value));

    }

    private static String toHex(byte input[]) {
        if (input == null) {
            return null;
        }
        StringBuilder output = new StringBuilder(input.length * 2);
        for (byte anInput : input) {
            int current = anInput & 0xff;
            if (current < 16) {
                output.append("0");
            }
            output.append(Integer.toString(current, 16));
        }

        return output.toString();
    }

    public static String HMACSHA256(String data, String key) {
        return HMACSHA256(data.getBytes(), key.getBytes());
    }

    public static String HMACSHA256(byte[] data, byte[] key) {
        try {
            SecretKeySpec signingKey = new SecretKeySpec(key, "HmacSHA256");
            Mac mac = Mac.getInstance("HmacSHA256");
            mac.init(signingKey);
            return byte2hex(mac.doFinal(data));
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        } catch (InvalidKeyException e) {
            e.printStackTrace();
        }
        return null;
    }

    public static String byte2hex(byte[] b) {
        StringBuilder hs = new StringBuilder();
        String stmp;
        for (int n = 0; b != null && n < b.length; n++) {
            stmp = Integer.toHexString(b[n] & 0XFF);
            if (stmp.length() == 1) {
                hs.append('0');
            }
            hs.append(stmp);
        }
        return hs.toString().toUpperCase();
    }



}
