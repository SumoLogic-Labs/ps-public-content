Main Fortinet fields can be extracted using the following FER:

```
| parse regex "action\=\"(?<action>[^\"]+)\"" nodrop
| parse regex "appcat\=\"(?<appcat>[^\"]+)\"" nodrop
| parse regex "catdesc\=\"(?<catdesc>[^\"]+)\"" nodrop
| parse regex "dstip\=(?<dstip>[^\s]+)" nodrop
| parse regex "dstport\=(?<dstport>\d+)" nodrop
| parse regex "eventsubtype\=\"(?<eventsubtype>[^\"]+)\"" nodrop
| parse regex "eventtype\=\"(?<eventtype>[^\"]+)\"" nodrop
| parse regex "group\=\"(?<group>[^\"]+)\"" nodrop
| parse regex "hostname\=\"(?<hostname>[^\"]+)\"" nodrop
| parse regex "msg\=\"(?<msg>[^\"]+)\"" nodrop
| parse regex "policyname\=\"?(?<policyname>[^\"]+)\"?\s*" nodrop
| parse regex "proto\=(?<proto>\d+)" nodrop
| parse regex "service\=\"(?<service>[^\"]+)\"" nodrop
| parse regex "srcip\=(?<srcip>[^\s]+)" nodrop
| parse regex "srcport\=(?<srcport>\d+)" nodrop
| parse regex "subtype\=\"(?<subtype>[^\"]+)\"" nodrop
| parse regex "type\=\"(?<type>[^\"]+)\"" nodrop
| parse regex "unauthuser\=\"(?<unauthuser>[^\"]+)\"" nodrop
| parse regex "url\=\"(?<url>[^\"]+)\"" nodrop
| parse regex "user\=\"(?<user>[^\"]+)\"" nodrop
| parse regex "vpntunnel\=\"(?<vpntunnel>[^\"]+)" nodrop
| parse regex "vpntype\=\"(?<vpntype>[^\"]+)\"" nodrop
```
