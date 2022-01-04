select column_name
from information_schema.columns
where table_schema = 'public'
  and table_name = 'm_qunar_hotel';

-- 消费分析
select time_stamp as summary_date, sum(amount) as total
from m_ylzh_industry_day
where time_stamp >= (current_date - interval '1 months')
  and region_name = '余杭区'
group by time_stamp
order by time_stamp;

-- 游客预定情况
SELECT *
from public.fn_yuhang_tourist_from('#{area}', '#{from}', '#{to}');

-- 高铁沿线的城市预定情况
SELECT *
from public.fn_yuhang_tourist_from('#{area}', '#{from}', '#{to}')
where area in ('上海', '南京', '宁波', '温州', '绍兴', '苏州', '金华', '诸暨', '桐乡', '嘉兴');

-- mock数据
insert into tr_traffic_subway_flow (name, entry_flow, exit_flow, start_time, end_time, business_day, tag, stat_id)
select name,
       entry_flow,
       exit_flow,
       replace(to_char(start_time, 'yyyy-MM-dd HH24:MI:SS'), '2021-10-21', '2021-11-06')::timestamp,
       replace(to_char(end_time, 'yyyy-MM-dd HH24:MI:SS'), '2021-10-21', '2021-11-06')::timestamp,
       replace(to_char(business_day, 'yyyy-MM-dd'), '2021-10-21', '2021-11-06')::timestamp,
       tag,
       160076408 + 4734 + (row_number() over ())
from tr_traffic_subway_flow
where business_day = '2021-10-21 00:00:00';

-- 订单人数
SELECT sum(order_count) * 13 as order_count, use_time
from m_qunar_hotel
where district = '余杭区'
  and use_time >= '2020-10-24'::date
  and use_time < '2021-11-24'::date
GROUP BY use_time;

-- 游客预定来源地的数据, mock 2021年9月8号到12月末数据
insert into m_qunar_train(departure_city, resident_city, order_count, person_count, male_count, female_count, age_0018,
                          age_1925, age_2635, age_3645, age_4655, age_56ab, order_with_children, order_without_children,
                          order_time, use_time)
select departure_city,
       resident_city,
       order_count,
       person_count,
       male_count,
       female_count,
       age_0018,
       age_1925,
       age_2635,
       age_3645,
       age_4655,
       age_56ab,
       order_with_children,
       order_without_children,
       replace(to_char(order_time, 'yyyy-MM-dd HH24:MI:SS'), '2020', '2021')::timestamp,
       replace(to_char(use_time, 'yyyy-MM-dd HH24:MI:SS'), '2020', '2021')::timestamp
from m_qunar_train
where to_char(order_time, 'yyyy-MM-dd') between '2020-09-08' and '2020-12-31';

-- 订单人数变化，需要mock2021年9月22号之后余杭区的数据
insert into m_qunar_hotel(hotel_name, order_count, district, address, hotel_rating, room_type, person_count,
                          resident_city, consumption_level, attribute, order_time, use_time, lng, lat, geometry,
                          resident_city_id, tr_hotel_id, source)
select hotel_name,
       order_count,
       district,
       address,
       hotel_rating,
       room_type,
       person_count,
       resident_city,
       consumption_level,
       attribute,
       replace(to_char(order_time, 'yyyy-MM-dd HH24:MI:SS'), '2020', '2021')::timestamp,
       replace(to_char(use_time, 'yyyy-MM-dd HH24:MI:SS'), '2020', '2021')::timestamp,
       lng,
       lat,
       geometry,
       resident_city_id,
       tr_hotel_id,
       source
from m_qunar_hotel
where to_char(order_time, 'yyyy-MM-dd') between '2020-09-22' and '2020-12-31';

-- 游客贡献度
SELECT (t1.a / t2.b)::float as ratio
from (select sum(person_count) * 9000::NUMERIC as a
      from m_qunar_hotel
      where use_time >= '#{from}'::date
        and use_time <= '#{to}'::date
        and district = '余杭区'
     ) t1,
     (select sum(value)::NUMERIC as b
      from n_dwd_scene_population_mobile_real_adjust
      where ts >= '#{from}'
        and ts <= '#{to}'
        and frequency_type = 'DAY'
        and level = '2'
        and obj_id = '330110'
     ) t2;

-- 提供余杭区的人流数据
select sum(person_count) * 9000::NUMERIC as a
from m_qunar_hotel
where use_time >= '2021-10-24'::date
  and use_time <= '2021-11-24'::date
  and district = '余杭区';

select sum(value)::NUMERIC as b
from n_dwd_scene_population_mobile_real_adjust
where ts >= '2021-10-24'
  and ts <= '2021-11-24'
  and frequency_type = 'DAY'
  and level = '2'
  and obj_id = '330110';

-- 消费分析 -
select time_stamp as summary_date, sum(amount) as total
from m_ylzh_industry_day
where time_stamp >= (current_date - interval '1 months')
  and region_name = '余杭区'
group by time_stamp
order by time_stamp;

-- 年龄占比
SELECT round((age_0018 * 100::float / age_total)::numeric,
             2) as age_0018_ratio,
       round((age_1925 * 100::float / age_total)::numeric,
             2) as age_1925_ratio,
       round((age_2635 * 100::float / age_total)::numeric,
             2) as age_2635_ratio,
       round((age_3645 * 100::float / age_total)::numeric,
             2) as age_3645_ratio,
       round((age_4655 * 100::float / age_total)::numeric,
             2) as age_4655_ratio,
       round((age_56ab * 100::float / age_total)::numeric,
             2) as age_56ab_ratio
from (
         SELECT sum(age_0018)                                                        as age_0018,
                sum(age_1925)                                                        as age_1925,
                sum(age_2635)                                                        as age_2635,
                sum(age_3645)                                                        as age_3645,
                sum(age_4655)                                                        as age_4655,
                sum(age_56ab)                                                        as age_56ab,
                sum(age_0018 + age_1925 + age_2635 + age_3645 + age_4655 + age_56ab) as age_total
         from m_qunar_vacation
         where use_time >= '2021-09-01'::date
           and use_time < '2021-10-01'::date) a;

-- 年龄占比
SELECT sum(age_0018)            as age_0018,
       sum(age_1925)            as age_1925,
       sum(age_2635)            as age_2635,
       sum(age_3645)            as age_3645,
       sum(age_4655)            as age_4655,
       sum(age_56ab)            as age_56ab,
       sum(age_0018 + age_1925) as age_total
from m_qunar_vacation
where use_time >= '2021-09-01'::date
  and use_time < '2021-10-01'::date;

-- 性别占比
select round((male_count * 100::float / (male_count + female_count))::numeric, 2)   as male_count_ratio,
       round((female_count * 100::float / (male_count + female_count))::numeric, 2) as female_count_ratio
from (
         SELECT sum(male_count) as male_count, sum(female_count) as female_count
         from m_qunar_vacation
         where use_time >= '2021-10-30'::date
           and use_time < '2021-11-30'::date) a;

SELECT sum(male_count) as male_count, sum(female_count) as female_count
from m_qunar_vacation
where use_time >= '2020-10-30'::date
  and use_time < '2020-11-30'::date;


-- 近30天游客量：旅游分析
select ts, value as sum
from n_dwd_scene_population_mobile_real_adjust
where ts >= CURRENT_DATE - interval '30 days'
  and obj_id = '330110'
  and frequency_type = 'DAY'
order by ts asc;

-- 住宿人流检测
select ts as checkin_time, stayin_num as num
from tr_police_hotel_checkin_stayin_ratio
where ts >= CURRENT_DATE - interval '30 days'
  and district_id = 330110
order by checkin_time asc;

-- 全域游客数据统计:景区人数统计
select sum(value)
from n_dwd_scene_population_mobile_real_adjust
where frequency_type = 'POINT'
  and level = 3
  and ts = (select max(ts)
            from n_dwd_scene_population_mobile_real_adjust
            where frequency_type = 'POINT'
              and level = 3
              and ts >= current_timestamp - interval '200 min');

select max(ts)
from n_dwd_scene_population_mobile_real_adjust
where frequency_type = 'POINT'
  and level = 3
  and ts >= current_timestamp - interval '600 min';


-- 文化点位实时游客数
select real.name as scene_name, gaode_lng as lng, gaode_lat as lat, value as hour_tourist_num
from n_dwd_scene_population_mobile_real_adjust real
         inner join n_dwd_scene_info info on info.code = real.obj_id
where frequency_type = 'POINT'
  and (type = '文化' or info.name like '%文化%' or info.name like '%院%')
  and real.level = 3
  and ts = (SELECT max(ts)
            from n_dwd_scene_population_mobile_real_adjust
            where level = 3
              and frequency_type = 'POINT'
              and ts >= current_timestamp - interval '60 min');

-- 轨迹重点景区
SELECT name, sum(value) as value
from (
         SELECT unnest(tour_line)::varchar as tour_line, sum(value) as value, come_time
         from n_dwd_scene_population_mobile_travel_line_more_three_scene
         where come_time::date >= '#{from}'
           and come_time <= '#{to}'
         GROUP BY tour_line, come_time
         order by value desc
         limit 50
     ) a
         inner join
     (select DISTINCT(code) AS code, name
      FROM tr_scene
      where code is not null
        and name in (SELECT unnest('#{code}'::varchar[])::varchar as tour_line)) b
     on a.tour_line = b.code
GROUP BY name
order BY value desc;

-- 游客来源
select *
from fn_yuhang_reavel_line_tourist_from('#{code}', '#{from}', '#{to}');

-- 消费变化
select time_stamp, sum(amount) as amount, sum(persons) as persons, sum(transactions) as transactions
from m_ylzh_industry_day
where time_stamp::date >= '#{from}'
  and time_stamp::date <= '#{to}'
group by time_stamp
order by time_stamp asc;

-- 夜间经济消费趋势
select a.date, round((c.sum_total * a.value1 / b.value2) / 10000::numeric, 2) as num
from (select time_stamp::date as date, sum(consumpe_num) as sum_total
      from m_ylzh_city_day
      where time_stamp <= '2021-11-25'
        and time_stamp >= '2020-10-25'
      group by time_stamp) c
         join
     (select time_stamp::date as date, sum(amount) as value1
      from m_ylzh_industry_day
      where main_industry in ('住宿服务业', '文化、体育和娱乐行业', '交通运输业', '旅游服务业', '零售行业', '餐饮业')
        and region_name = '余杭区'
        and time_stamp <= '2021-11-25'
        and time_stamp >= '2020-10-25'
      group by time_stamp) a
     on c.date = a.date
         join
     (select time_stamp::date as date, sum(amount) as value2
      from m_ylzh_industry_day
      where region_name = '余杭区'
        and time_stamp <= '2021-11-25'
        and time_stamp >= '2020-10-25'
      group by time_stamp) b
     on a.date = b.date;


-- 消费偏好分析


select sub_industry, sum(amount) / 10000::numeric as value
from m_ylzh_industry_day
where main_industry in ('住宿服务业', '文化、体育和娱乐行业', '交通运输业', '旅游服务业', '零售行业', '餐饮业')
  and time_stamp <= '2021-11-25'
  and time_stamp >= '2021-09-25'
  and region_name = '余杭区'
group by sub_industry
order by value desc;

-- 游客画像分析
select type, id, value
from (select (b.rec).key::varchar as type,
             case
                 when (b.rec).key = '男' then 1
                 else 2 end       as id,
             (b.rec).value::int,
             '客源'                 as tag
      from (
               select jsonb_each(row_to_json(a)::jsonb) as rec
               from (select sum(male_count) as "男", sum(female_count) as "女"
                     from m_qunar_vacation
                     where use_time >= '2021-10-25'::date
                       and use_time <= '2021-11-25'::date) a
           ) b

      union all

      select case when type = '1' then '男' else '女' end as type,
             case when type = '1' then 1 else 2 end     as id,
             sum(value)                                 as value,
             '住宿'                                       as tag
      from n_dws_hotel_portrait_d main,
           tr_police_hotel_info info
      where main.hotel_id = info.id
        and ts >= '2021-10-25'
        and ts <= '2021-11-25'
        and tag = 'xb'
        and type is not null
      group by type
      order by id) t

where tag = '客源';
--
select jsonb_each(row_to_json(a)::jsonb) as rec
from (select sum(male_count) as "男", sum(female_count) as "女"
      from m_qunar_vacation
      where use_time >= '2021-10-25'::date
        and use_time <= '2021-11-25'::date) a;

select row_to_json(a)
from (select sum(male_count) as 男, sum(female_count) as 女
      from m_qunar_vacation
      where use_time >= '2021-10-25'::date
        and use_time <= '2021-11-25'::date) a;


-- 年龄占比
select type, id, value
from (select (b.rec).key::varchar as type,
             case
                 when (b.rec).key = '18岁及以下' then 1
                 when (b.rec).key = '19~25岁' then 2
                 when (b.rec).key = '26~35岁' then 3
                 when (b.rec).key = '36~45岁' then 4
                 when (b.rec).key = '46~55岁' then 5
                 else 6 end       as id,
             (b.rec).value::int,
             '客源'                 as tag
      from (
               select jsonb_each(row_to_json(a)::jsonb) as rec
               from (select sum(age_0018) as "18岁及以下",
                            sum(age_1925) as "19~25岁",
                            sum(age_2635) as "26~35岁",
                            sum(age_3645) as "36~45岁",
                            sum(age_4655) as "46~55岁",
                            sum(age_56ab) as "56岁及以上"
                     from m_qunar_vacation
                     where use_time >= '2021-10-25'::date
                       and use_time <= '2021-11-25'::date) a
           ) b

      union all

      select case
                 when type = '1' then '19岁及以下'
                 when type = '2' then '20~29岁'
                 when type = '3' then '30~39岁'
                 when type = '4' then '40~49岁'
                 when type = '5' then '50~59岁'
                 else '60岁及以上' end as type,
             case
                 when type = '1' then 1
                 when type = '2' then 2
                 when type = '3' then 3
                 when type = '4' then 4
                 when type = '5' then 5
                 else 6 end        as id,
             sum(value)            as value,
             '住宿'                  as tag
      from n_dws_hotel_portrait_d main,
           tr_police_hotel_info info
      where main.hotel_id = info.id
        and ts >= '2021-10-25'
        and ts <= '2021-11-25'
        and tag = 'age'
        and type is not null
      group by type
      order by id) t

where tag = '客源';

-- 酒店入住排名
select info.district_id, district, info.hotel_name, checkin_ratio, ts
from (select fusion_id, district, occupancy_num::float * 100 as checkin_ratio, ts
      from n_dws_hotel_checkin_hotel_day
      where ts = current_date - interval '100 day'
        and occupancy_num::float < 1
        and occupancy_num != '--') main,
     (select id, hotel_name, district_id from n_dwd_hotel_info where ota_level > 1 and district_id = 330110) info
where info.id = main.fusion_id
ORDER BY checkin_ratio desc
limit 10;

-- 酒店好评变化率
select count(1), to_char(pub_time, 'yyyy-MM') as mon
from (select hotel_id, pub_time
      from n_dwd_hotel_comment_label
      where pub_time > (select current_date - interval '6 mons')
        and sentiment = 2
        and abstract != '') main,
     (select id from n_dwd_hotel_info where district_id = 330110) info
where main.hotel_id = info.id
group by mon
order by mon desc
limit 6;

select hotel_id, pub_time
from n_dwd_hotel_comment_label
where pub_time > (select current_date - interval '6 mons')
  and sentiment = 2
  and abstract != '';

select id
from n_dwd_hotel_info
where district_id = 330110;

-- 区县热度分析
select ts + interval '2 mons' + interval '3 days' as ts, keyword, index_value, #{
from} as
from, #{to} as to
from tr_trend_baidu_index
where keyword in ('富阳'
    , '余杭'
    , '桐庐')
  and ts>=(select max(ts) - interval '30 days' from tr_trend_baidu_index
    where keyword in ('富阳'
    , '余杭'
    , '桐庐'))
  and ts
    < current_date
order by ts;

-- 实时游客变化
select ts, sum(value)
from (select ts, value, obj_id
      from n_dwd_scene_population_mobile_real_adjust
      where frequency_type = 'POINT'
        and ts >= (select max(ts)
                   from n_dwd_scene_population_mobile_real_adjust
                   where ts >= CURRENT_TIMESTAMP - interval '40 min')) main
where main.obj_id = 'S10006'
group by ts
order by ts;

select code
from n_dwd_scene_info info
where district_id = 330110
  and info.id = 167;

select max(ts)
from n_dwd_scene_population_mobile_real_adjust
where ts >= CURRENT_TIMESTAMP - interval '40 min';

select ts, value, obj_id
from n_dwd_scene_population_mobile_real_adjust
where frequency_type = 'POINT'
  and ts >= (select max(ts)
             from n_dwd_scene_population_mobile_real_adjust
             where ts >= CURRENT_TIMESTAMP - interval '40 min');

select ts, tourism_balance
from n_dws_tourism_balance
where district = '余杭区'
  and ts >= current_date
order by ts;

-- 过夜游客比重数据
select round(COUNT(*)::numeric / value::numeric, 2) as ratio,
       COUNT(*),
       checkin_time + interval '61 days'            as checkin_time
from tr_police_hotel_day_info main,
     (select value, ts
      FROM tr_scene_population_mobile_real
      where obj_id = '330110'
        AND frequency_type = 'DAY'
        and ts between '2020-09-01 00:00:00' and
          '2020-09-25 00:00:00') t
where main.checkin_time = t.ts
  and checkin_time between '2020-09-01 00:00:00' and
    '2020-09-25 00:00:00'
  and district_id = '330110'
group by checkin_time, value;

-- 天级游客变化
select name, value, lng, lat, null as description
from n_dwd_scene_population_mobile_real_adjust
where level = 3
  and frequency_type = 'POINT'
  and ts > current_timestamp - interval '40 min'
  and ts =
      (select max(ts)
       from n_dwd_scene_population_mobile_real_adjust
       where frequency_type = 'POINT'
         and level = 3
         and ts >= current_timestamp - interval '40 min');

select max(ts)
from n_dwd_scene_population_mobile_real_adjust
where frequency_type = 'POINT'
  and level = 3
  and ts >= current_timestamp - interval '40 min';

-- 景区实时客流
select a.name, value, peak, (value / peak::float)::FLOAT as ratio
from (
         SELECT name, value
         from n_dwd_scene_population_mobile_real_adjust
         where ts >= (select max(ts)
                      from n_dwd_scene_population_mobile_real_adjust
                      where ts >= current_timestamp - interval '1 hour'
                        and frequency_type = 'POINT')
           and frequency_type = 'POINT') a
         inner join(
    SELECT name, (extra ->> 'peak') as peak
    from n_dwd_scene_info
    where district_id = 330110
      and type in ('景区', '文化')) b
                   on a.name = b.name
order by ratio desc;

select a.name, value
from (
         SELECT name, value
         from n_dwd_scene_population_mobile_real_adjust
         where ts >= (select max(ts)
                      from n_dwd_scene_population_mobile_real_adjust
                      where ts >= current_timestamp - interval '1 hour'
                        and frequency_type = 'POINT')
           and frequency_type = 'POINT') a;

-- 景区客流预测
SELECT name,
       future_value,
       CASE
           WHEN future_value > now_value THEN 'up_trend'
           ELSE 'down_trend'
           END as tread,
       CASE
           WHEN (future_value - now_value) * 100::float / now_value > 20 THEN '大于20'
           ELSE '小于20'
           END as amplification
from (
         SELECT b.name, a.value as now_value, c.value as future_value
         from (SELECT name, value
               from n_dwd_scene_population_mobile_real_adjust
               where ts = (select max(ts)
                           from n_dwd_scene_population_mobile_real_adjust
                           where frequency_type = 'POINT'
                             and ts >= current_timestamp - interval '60 min')
                 and frequency_type = 'POINT'
               order by value desc) a
                  inner join
              (SELECT code, name from n_dwd_scene_info where district_id = 330110 and code is not null) b
              on a.name = b.name
                  inner join
              (select tfcunit_id, traveller_cnt as value
               from dws_tfc_state_tfcunit_tp_prdtptravellercnt_rt
               where data_step_time_tp = (select max(data_step_time_tp)
                                          from dws_tfc_state_tfcunit_tp_prdtptravellercnt_rt
                                          where data_step_time_tp >= current_timestamp - interval '2 hour')) c
              on b.code = c.tfcunit_id
         order by future_value desc) a
order by future_value desc;

-- 余杭高铁站
select COALESCE(sum(getoff::int), 0) as value
from tr_jiaotong_check_real_num
where station_name = '余杭'
  and train_no in (
    SELECT train_no
    from n_dwd_jiaotong_station_info2020
    where train_name = '余杭站'
      and to_timestamp((current_date::varchar || train_down), 'YYYY-MM-ddHH24:MI:ss') >= now() - interval '30 min'
      and to_timestamp((current_date::varchar || train_down), 'YYYY-MM-ddHH24:MI:ss') <= now());

-- mock数据到2021年末
insert into tr_jiaotong_check_real_num(station_name, station_no, station_telecode, station_train_code, train_date,
                                       train_no, count_person, getoff, geton, ts)
select station_name,
       station_no,
       station_telecode,
       station_train_code,
       replace(train_date, '2020', '2021'),
       train_no,
       count_person,
       getoff,
       geton,
       replace(to_char(ts, 'yyyy-mm-dd hh24:mi:ss'), '2020', '2021')::timestamp
from tr_jiaotong_check_real_num
where ts between '2020-01-05' and '2020-12-31';

SELECT SUM(GETOFF) as sum_getoff, SUM(GETON) as sum_geton, train_date
FROM tr_jiaotong_check_real_num
WHERE station_name = '余杭'
  and train_date::date >= current_date - interval '30' day
GROUP BY train_date;


select t.toll_name, t.e_type, t.e_count, t.e_date::TIMESTAMP
from m_transport_highway main
         right join (select *, ROW_NUMBER() OVER (partition by e_date,toll_name,e_type order by e_count desc) as rnum
                     from m_transport_highway
                     where e_date >= '2019-05-01'
                       AND e_date <= '2019-05-25'
                       AND area = '余杭区') t ON main.id = t.id
where rnum <= 1;

select ts      as ts,
       keyword,
       index_value,
       'form'  as
                  from,
       '#{to}' as to
from tr_trend_baidu_index
where keyword in ('富阳', '余杭', '桐庐')
  and ts >= current_date - interval '30 days'
  and ts < current_date
order by ts;

select current_timestamp - interval '1' year;
select current_timestamp - interval '2' month;
select current_timestamp - interval '3' day;
select current_timestamp - interval '4' hour;
select current_timestamp - interval '5' minute;
select current_timestamp - interval '600' second;

select ts, keyword, index_value
from tr_trend_baidu_index
where keyword in ('余杭')
  and ts >= '2021-06-01'
  and ts <= '2021-12-01'
order by ts asc, keyword asc;

select count(*)
from tr_trend_baidu_index;


SELECT train_no
from n_dwd_jiaotong_station_info2020
where train_name = '余杭站'
  and to_timestamp((current_date::varchar || train_down), 'YYYY-MM-ddHH24:MI:ss') >= now() - interval '30 min'
  and to_timestamp((current_date::varchar || train_down), 'YYYY-MM-ddHH24:MI:ss') <= now();

-- 地铁
select name, exit_flow as value
from (
         SELECT name, exit_flow, row_number() over (PARTITION BY name order BY start_time desc)
         from tr_traffic_subway_flow
         where start_time >= '2020-10-05'
           and name in ('乔司站',
                        '金家渡站',
                        '五常站',
                        '白洋站',
                        '访溪路站',
                        '永福站',
                        '杜甫村站',
                        '联胜路站',
                        '杭师大仓前站',
                        '良渚站',
                        '天都城站',
                        '高教路站',
                        '乔司南站',
                        '良睦路站',
                        '创远路站',
                        '良睦路站',
                        '星桥路站',
                        '绿汀路站',
                        '翁梅站',
                        '文一西路站',
                        '余杭高铁站站',
                        '南苑站',
                        '临平站',
                        '邱山大街站',
                        '东湖站',
                        '玉架山站',
                        '龙安湖站',
                        '储运路站',
                        '杭行路站',
                        '祥园路站',
                        '勾阳路站',
                        '吴家路站',
                        '阿里巴巴站',
                        '新兴路站',
                        '火车西站站',
                        '苕溪站',
                        '创景路站',
                        '葛巷站',
                        '凤新路站',
                        '金星站',
                        '禹航路站',
                        '中泰站',
                        '南湖站',
                        '南峰站')) a
where row_number = 1;

-- 高速收费站
SELECT sum(e_count) as value
from m_transport_highway
where area = '余杭区'
  and e_type = 1
  and create_time::date = current_date - interval '2 year';

-- 数据在线
select sum(visit_pv)                                       as visit_count,
       sum(visit_uv)                                       as visit_pepole_count,
       sum((visit_pv * (stay_time_uv / 3600::float)))::int as visit_time
from yuhang.n_dwd_applets_trend_d
where ts >= '#{ts}';

-- 停车场分析
select a.name,
       a."level",
       max_tourist,
       total_berth,
       round((tourist_value::float / total_berth / 3)::numeric, 2) as out_ratio
from (
         select a.name, a."level", sum(total_berth) as total_berth
         from (
                  select name, "level", array_agg(parking_id) as parking_ids
                  from (SELECT name, gaode_lng, gaode_lat, "level"
                        from n_dwd_scene_info
                        where district_id = 330110
                          and gaode_lng is not null) a
                           inner join
                       (select parking_id, parking_name, gmap_lng, gmap_lat from n_dwd_chengguan_parking_info) b
                       on ST_Distance(ST_Point(gmap_lng, gmap_lat)::geography,
                                      ST_Point(gaode_lng, gaode_lat)::geography) <= 500
                  GROUP BY name, "level"
              ) a
                  inner join
              (
                  select DISTINCT parking_id, total_berth
                  from n_dwd_chengguan_parking_berth_related
                  where ts > current_date
              ) b
              on b.parking_id = any (parking_ids)
         GROUP BY a.name, "level"
     ) a
         inner join
     (select name, MAX(value) as max_tourist
      from n_dwd_scene_population_mobile_real_adjust
      where ts > '2020-10-02'
        and ts < '2020-10-04'
        and frequency_type = 'POINT'
        and district_id = 330110
        and name != '余杭区'
      group by name) c
     on a.name = c.name
         inner join
     (select name, value as tourist_value
      from n_dwd_scene_population_mobile_real_adjust
      where ts = (select max(ts)
                  from n_dwd_scene_population_mobile_real_adjust
                  WHERE frequency_type = 'POINT'
                    and district_id = 330110
                    and name != '余杭区'
                    and ts >= current_date - interval '2 hours')
        and frequency_type = 'POINT'
        and district_id = 330110) d
     on a.name = d.name;

-- 盲点分析
select e.*,
       case when ratio < 10 then '低' when 10 <= ratio and ratio <= 100 then '中' else '高' end as deficiency,
       case when ratio < 10 then '高' when 10 <= ratio and ratio <= 100 then '中' else '低' end as busload
from (
         select c.*, d.value / c.count / 3::float as ratio
         from (select a.name, a.level, a.peak, count(b.name)
               from (select name, level, extra ->> 'peak' as peak, gaode_lng as lng, gaode_lat as lat
                     from n_dwd_scene_info
                     where district_id = 330110
                       and mobile_collection = '1') a,
                    (select name, lng, lat from m_poi_330100 where object_type = '150500' and region_id = 330110) b
               where ST_Distance(ST_Point(a.lng, a.lat)::geography, ST_Point(b.lng, b.lat)::geography) <=#{distince}
               group by a.name, a.level, a.peak) c,
              (select name, value
               from n_dwd_scene_population_mobile_real_adjust
               where ts = (select max(ts)
                           from n_dwd_scene_population_mobile_real_adjust
                           WHERE frequency_type = 'POINT'
                             and district_id = 330110
                             and name != '余杭区'
                             and ts >= current_date - interval '2 hours')
                 and frequency_type = 'POINT'
                 and district_id = 330110) d
         where c.name = d.name
     ) e

union

select e.*, '高' as deficiency, '低' as busload
from (
         select c.*, d.value / c.count / 3::float as ratio
         from (select a.name, a.level, a.peak, count(b.name)
               from (select name, level, extra ->> 'peak' as peak, gaode_lng as lng, gaode_lat as lat
                     from n_dwd_scene_info
                     where district_id = 330110
                       and mobile_collection = '1') a,
                    (select name, lng, lat from m_poi_330100 where object_type = '150500' and region_id = 330110) b
               where ST_Distance(ST_Point(a.lng, a.lat)::geography, ST_Point(b.lng, b.lat)::geography) >#{distince}
               group by a.name, a.level, a.peak) c,
              (select name, value
               from n_dwd_scene_population_mobile_real_adjust
               where ts = (select max(ts)
                           from n_dwd_scene_population_mobile_real_adjust
                           WHERE frequency_type = 'POINT'
                             and district_id = 330110
                             and name != '余杭区'
                             and ts >= current_date - interval '2 hours')
                 and frequency_type = 'POINT'
                 and district_id = 330110) d
         where c.name = d.name
     ) e;

select e.*, '高' as deficiency, '低' as busload
from (
         select c.*, d.value / c.count / 3::float as ratio
         from (select a.name, a.level, a.peak, count(b.name)
               from (select name, level, extra ->> 'peak' as peak, gaode_lng as lng, gaode_lat as lat
                     from n_dwd_scene_info
                     where district_id = 330110
                       and mobile_collection = '1') a,
                    (select name, lng, lat from m_poi_330100 where object_type = '150500' and region_id = 330110) b
               where ST_Distance(ST_Point(a.lng, a.lat)::geography, ST_Point(b.lng, b.lat)::geography) > 1000
               group by a.name, a.level, a.peak) c,
              (select name, value
               from n_dwd_scene_population_mobile_real_adjust
               where ts = (select max(ts)
                           from n_dwd_scene_population_mobile_real_adjust
                           WHERE frequency_type = 'POINT'
                             and district_id = 330110
                             and name != '余杭区'
                             and ts >= current_date - interval '2 hours')
                 and frequency_type = 'POINT'
                 and district_id = 330110) d
         where c.name = d.name
     ) e;

--
-- 余杭高铁站:
SELECT SUM(GETOFF) as sum_getoff, SUM(GETON) as sum_geton, train_date
FROM tr_jiaotong_check_real_num
WHERE station_name = '余杭'
  and train_date::date >= '2020-12-08'
  and train_date::date <= '2021-01-08'
GROUP BY train_date;

select train_date::date as time_data
from tr_jiaotong_check_real_num;

-- 余杭收费站
select *
from m_transport_highway;

-- 开始进行数据mock操作
-- mock例子:
insert into tr_traffic_subway_flow (name, entry_flow, exit_flow, start_time, end_time, business_day, tag, stat_id)
select name,
       entry_flow,
       exit_flow,
       replace(to_char(start_time, 'yyyy-MM-dd HH24:MI:SS'), '2021-10-21', '2021-11-06')::timestamp,
       replace(to_char(end_time, 'yyyy-MM-dd HH24:MI:SS'), '2021-10-21', '2021-11-06')::timestamp,
       replace(to_char(business_day, 'yyyy-MM-dd'), '2021-10-21', '2021-11-06')::timestamp,
       tag,
       160076408 + 4734 + (row_number() over ())
from tr_traffic_subway_flow
where business_day = '2021-10-21 00:00:00';

-- 来源地排名
SELECT *
from public.fn_yuhang_tourist_from('#{area}', '#{from}', '#{to}');

-- 对游客预定来源进行mock
insert into m_qunar_vacation(resident_city, order_count, person_count, male_count, female_count, age_0018, age_1925,
                             age_2635, age_3645, age_4655, age_56ab, order_with_children, order_without_children,
                             travel_mode, avg_days, avg_price, sightseeing_line, order_time, use_time)

select resident_city,
       order_count,
       person_count,
       male_count,
       female_count,
       age_0018,
       age_1925,
       age_2635,
       age_3645,
       age_4655,
       age_56ab,
       order_with_children,
       order_without_children,
       travel_mode,
       avg_days,
       avg_price,
       sightseeing_line,
       replace(to_char(use_time, 'yyyy-mm-dd hh24:mi:ss'), '2020', '2021')::timestamp,
       replace(to_char(order_time, 'yyyy-mm-dd hh24:mi:ss'), '2020', '2021')::timestamp
from m_qunar_vacation
where use_time between '2020-09-23' and '2020-12-31';

select round((male_count * 100::float / (male_count + female_count))::numeric, 2)   as male_count_ratio,
       round((female_count * 100::float / (male_count + female_count))::numeric, 2) as female_count_ratio
from (
         SELECT sum(male_count) as male_count, sum(female_count) as female_count
         from m_qunar_vacation
         where use_time between '2021-10-31' and '2021-10-31') a;

select *
from m_qunar_train
where order_time > '2021-09-09';

/*
游客预定来源排名，高铁沿线
*/
SELECT *
from public.fn_yuhang_tourist_from('city', '2021-10-29', '2021-11-29')
where area in ('上海市', '南京市', '宁波市', '温州市', '绍兴市', '苏州市', '金华市', '诸暨市', '桐乡市', '嘉兴市');

-- 函数里面的b.name 需要替换为a.city
select sum(a.count)::int, a.city, b.lng::varchar, b.lat::varchar
from (
         SELECT a.count * 13                    as count,
                a.departure_city                as city,
                m_region.lng,
                m_region.lat,
                SPLIT_PART(merger_name, ',', 2) as province
         from (SELECT count(order_count), departure_city
               FROM m_qunar_train
               where order_time >= '2021-10-29'::date
                 and order_time <= '2021-11-29'::date
                 and resident_city = '杭州'
               GROUP BY departure_city) a
                  left join
                  (select * from m_region where level_type = 2) m_region
                  on m_region.name like '%' || a.departure_city || '%'
         order by count desc) a

         LEFT JOIN

         (select * from m_region where level_type = 1) b
         on b.name like '%' || a.province || '%'

WHERE a.city is NOT NULL
GROUP BY a.city, b.lng, b.lat;

SELECT (a.count * 13)::int as count, a.departure_city as city, m_region.lng::varchar, m_region.lat::varchar
from (SELECT count(order_count), departure_city
      FROM m_qunar_train
      where order_time >= '2021-10-29'::date
        and order_time <= '2021-11-29'::date
        and resident_city = '杭州'
      GROUP BY departure_city) a
         left join
         (select * from m_region where level_type = 2) m_region
         on m_region.name like '%' || a.departure_city || '%'
order by count desc;

select max(order_count)
from m_qunar_train
group by departure_city;

select count(*), departure_city
from m_qunar_train
group by departure_city;

select sub.departure_city, sub.num
from (select count(*) as num, departure_city
      from m_qunar_train
      group by departure_city) sub
where sub.num > 13;

select count(*) as num, departure_city
from m_qunar_train
group by departure_city
having count(*) > 13;


-- 订单人数变化mock
SELECT sum(order_count) * 13 as order_count, use_time
from m_qunar_hotel
where district = '余杭区'
  and use_time >= '#{from}'::date
  and use_time < '#{to}'::date
GROUP BY use_time
order by use_time asc;

SELECT (t1.a / t2.b)::float as ratio
from (select sum(person_count) * 9000::NUMERIC as a
      from m_qunar_hotel
      where use_time >= '2021-10-29'::date
        and use_time <= '2021-11-29'::date
        and district = '余杭区'
     ) t1,
     (select sum(value)::NUMERIC as b
      from n_dwd_scene_population_mobile_real_adjust
      where ts >= '2021-10-29'
        and ts <= '2021-11-29'
        and frequency_type = 'DAY'
        and level = '2'
        and obj_id = '330110'
     ) t2;

select sum(person_count) * 9000::NUMERIC as a
from m_qunar_hotel
where use_time >= '2021-10-29'::date
  and use_time <= '2021-11-29'::date
  and district = '余杭区';

select sum(value)::NUMERIC as b
from n_dwd_scene_population_mobile_real_adjust
where ts >= '2021-10-29'
  and ts <= '2021-11-29'
  and frequency_type = 'DAY'
  and level = '2'
  and obj_id = '330110';


select time_stamp as summary_date, sum(amount) as total
from m_ylzh_industry_day
where time_stamp >= (current_date - interval '1 months')
  and region_name = '余杭区'
group by time_stamp
order by time_stamp;


SELECT round((age_0018 * 100::float / (age_0018 + age_1925 + age_2635 + age_3645 + age_4655 + age_56ab))::numeric,
             2) as age_0018_ratio,
       round((age_1925 * 100::float / (age_0018 + age_1925 + age_2635 + age_3645 + age_4655 + age_56ab))::numeric,
             2) as age_1925_ratio,
       round((age_2635 * 100::float / (age_0018 + age_1925 + age_2635 + age_3645 + age_4655 + age_56ab))::numeric,
             2) as age_2635_ratio,
       round((age_3645 * 100::float / (age_0018 + age_1925 + age_2635 + age_3645 + age_4655 + age_56ab))::numeric,
             2) as age_3645_ratio,
       round((age_4655 * 100::float / (age_0018 + age_1925 + age_2635 + age_3645 + age_4655 + age_56ab))::numeric,
             2) as age_4655_ratio,
       round((age_56ab * 100::float / (age_0018 + age_1925 + age_2635 + age_3645 + age_4655 + age_56ab))::numeric,
             2) as age_56ab_ratio
from (
         SELECT sum(age_0018) as age_0018,
                sum(age_1925) as age_1925,
                sum(age_2635) as age_2635,
                sum(age_3645) as age_3645,
                sum(age_4655) as age_4655,
                sum(age_56ab) as age_56ab
         from m_qunar_vacation
         where use_time >= '2021-10-30'::date
           and use_time < '2021-11-30'::date) a;


select ts as checkin_time, stayin_num as num
from tr_police_hotel_checkin_stayin_ratio
where ts >= CURRENT_DATE - interval '30 days'
  and district_id = 330110
order by checkin_time asc;

select info.id,
       info.name,
       value,
       longitude_84                      as lng,
       latitude_84                       as lat,
       value / (extra ->> 'peak')::float as ratio,
       extra ->> 'peak'                  as peak
from n_dwd_scene_population_mobile_real_adjust main,
     n_dwd_scene_info info
where main.obj_id = info.code
  and mobile_collection = '1'
  and info.district_id = 330110
  and frequency_type = 'POINT'
  and ts =
      (select max(ts)
       from n_dwd_scene_population_mobile_real_adjust
       where frequency_type = 'POINT'
         and level = 3
         and info.district_id = 330110
         and ts >= current_timestamp - interval '60 mins')
  and info.id not in (68, 1169);

select sum(value)
from n_dwd_scene_population_mobile_real_adjust
where frequency_type = 'POINT'
  and level = 3
  and ts = (select max(ts)
            from n_dwd_scene_population_mobile_real_adjust
            where frequency_type = 'POINT'
              and level = 3
              and ts >= current_timestamp - interval '120 min');


select *
from (
         select main.name, null as desc, value / (extra ->> 'peak')::float as ratio, '景区' as tag
         from n_dwd_scene_population_mobile_real_adjust main,
              n_dwd_scene_info info
         where main.obj_id = info.code
           and mobile_collection = '1'
           and info.district_id = 330110
           and frequency_type = 'POINT'
           and ts = (select max(ts)
                     from n_dwd_scene_population_mobile_real_adjust
                     where frequency_type = 'POINT'
                       and level = 3
                       and district_id = 330110
                       and ts >= current_date - interval '40min')
           and info.id not in (1169, 68)
           and type = '景区') t


union

select name, description as desc, null as ratio, '路况' as tag
from (
         select name, description, row_number() over (partition by name order by create_time desc) as num
         from n_ods_road_traffic
         where create_time > now() - interval '20 day'
           and name in
               ('太上路', '龙皇路', '长径线', '木桥浜路', '漕雅线', '莫干山路', '东西大道', '良熟路', '星河南路', '朝阳西路', '后枯线', '闲林山路', '南大街', '广和街',
                '东湖南路', '人民大道', '漕雅线', '沿溪路', '潘双线', '东明山路', '莫干山路', '美丽洲路', '良睦路', '练杭高速', '长径线', '美丽洲路', '梧桐圩路',
                '小白线', '龙超路', '圆满路', '后汤线', '望梅路', '汀雨路')) t
where t.num = 1

order by tag asc;

-- 消费分析总金额
select summary_date::timestamp, sum(value::float) as total
from (
         select summary_date, consume::json ->> '{tag}' as value
         from yuhang.tr_meituan_330110
         where granularity = 1
           and summary_date >= '{from}'::timestamp - interval '1 mons'
           and summary_date <= '{to}'::timestamp - interval '1 mons'
     ) t
group by summary_date
order by summary_date asc
limit 10;

-- 轨迹重点景区
insert into yuhang.tr_meituan_330110(summary_date, resident, granularity, type, sale, province, city, persona, consume,
                                     comment, status)
select replace(to_char(summary_date, 'yyyy-mm-dd hh24:mi:ss'), '2020', '2021')::timestamp,
       resident,
       granularity,
       type,
       sale,
       province,
       city,
       persona,
       consume,
       comment,
       status
from yuhang.tr_meituan_330110
where summary_date between '2020-01-30' and '2020-12-31'
  and granularity = 1;

select max(id)
from yuhang.tr_meituan_330110;
-- 1584436

select nextval('yuhang.tr_meituan_330110_id_seq');
-- 1353145

select setval('yuhang.tr_meituan_330110_id_seq', 1584437);

select time_stamp, main_industry, sum(amount)
from m_ylzh_industry_month
where time_stamp =
      (select max(time_stamp) from m_ylzh_industry_month where time_stamp > (current_date - interval '20 months'))
  and region_name = '余杭区'
  and main_industry in ('住宿服务业', '零售行业', '餐饮业', '交通运输业', '文化、体育和娱乐行业', '旅游服务业')
group by time_stamp, main_industry;

-- 重点景区游客监控
select info.id,
       info.name,
       value,
       longitude_84                      as lng,
       latitude_84                       as lat,
       value / (extra ->> 'peak')::float as ratio,
       extra ->> 'peak'                  as peak
from n_dwd_scene_population_mobile_real_adjust main,
     n_dwd_scene_info info
where main.obj_id = info.code
  and mobile_collection = '1'
  and info.district_id = 330110
  and frequency_type = 'POINT'
  and ts =
      (select max(ts)
       from n_dwd_scene_population_mobile_real_adjust
       where frequency_type = 'POINT'
         and level = 3
         and info.district_id = 330110
         and ts >= current_timestamp - interval '600 mins')
  and info.id not in (68, 1169);

SELECT name, sum(value) as value
from (
         SELECT unnest(tour_line)::varchar as tour_line, sum(value) as value, come_time
         from n_dwd_scene_population_mobile_travel_line_more_three_scene
         where come_time::date >= '2021-11-01'
           and come_time <= '2021-12-01'
         GROUP BY tour_line, come_time
         order by value desc
         limit 50
     ) a
         inner join
     (select DISTINCT(code) AS code, name
      FROM tr_scene
      where code is not null
        and name in (SELECT unnest('{杭州大剧院,都锦生织锦博物馆,湖滨街道,湖滨国际步行街区}'::varchar[])::varchar as tour_line)) b
     on a.tour_line = b.code
GROUP BY name
order BY value desc;

-- 重点轨迹景区
SELECT name, sum(value) as value
from (
         SELECT unnest(tour_line)::varchar as tour_line, sum(value) as value, come_time
         from n_dwd_scene_population_mobile_travel_line_more_three_scene
         where come_time::date >= '2021-10-01'
           and come_time <= '2021-12-01'
         GROUP BY tour_line, come_time
         order by value desc
         limit 50
     ) a
         inner join
     (select DISTINCT(code) AS code, name
      FROM tr_scene
      where code is not null
        and name in (SELECT unnest('{杭州大剧院,都锦生织锦博物馆,湖滨街道,湖滨国际步行街区}'::varchar[])::varchar as tour_line)) b
     on a.tour_line = b.code
GROUP BY name
order BY value desc;

select *
from fn_yuhang_reavel_line_tourist_from('#{code}', '#{from}', '#{to}');

select *
from (select from_prov,
             prov,
             city,
             amount,
             amount / sum(amount) over ()                               as ratio,
             lng,
             lat,
             ROW_NUMBER() over (partition by prov order by amount desc) as rnum
      from (select case from_prov when '浙江省' then '省内' else '省外' end as prov,
                   from_city                                         as city,
                   sum(amount)                                       as amount,
                   from_prov,
                   m.lng,
                   m.lat
            from m_ylzh_industry_month mon,
                 m_region m
            where region_name = '余杭区'
              and mon.from_city = m.name
              and time_stamp >= '2021-11-01'
              and time_stamp <= '2021-12-01'
              and from_prov != from_city
              and m.lng is not null
            group by prov, city, from_prov, m.lng, m.lat) t) t
where rnum <= 20;

select case from_prov when '浙江省' then '省内' else '省外' end as prov,
       from_city                                         as city,
       sum(amount)                                       as amount,
       from_prov,
       m.lng,
       m.lat
from m_ylzh_industry_month mon,
     m_region m
where region_name = '余杭区'
  and mon.from_city = m.name
  and time_stamp >= '2021-11-01'
  and time_stamp <= '2021-12-01'
  and from_prov != from_city
  and m.lng is not null
group by prov, city, from_prov, m.lng, m.lat;


-- 年龄/性别 占比
select type, id, value
from (select (b.rec).key::varchar as type,
             case
                 when (b.rec).key = '男' then 1
                 else 2 end       as id,
             (b.rec).value::int,
             '客源'                 as tag
      from (
               select jsonb_each(row_to_json(a)::jsonb) as rec
               from (select sum(male_count) as "男", sum(female_count) as "女"
                     from m_qunar_vacation
                     where use_time >= '2021-11-01'::date
                       and use_time <= '2021-12-01'::date) a
           ) b

      union all

      select case when type = '1' then '男' else '女' end as type,
             case when type = '1' then 1 else 2 end     as id,
             sum(value)                                 as value,
             '住宿'                                       as tag
      from n_dws_hotel_portrait_d main,
           tr_police_hotel_info info
      where main.hotel_id = info.id
        and ts >= '2021-11-01'
        and ts <= '2021-12-01'
        and tag = 'xb'
        and type is not null
      group by type
      order by id) t

where tag = '住宿';


select case when type = '1' then '男' else '女' end as type,
       case when type = '1' then 1 else 2 end     as id,
       sum(value)                                 as value,
       '住宿'                                       as tag
from n_dws_hotel_portrait_d main,
     tr_police_hotel_info info
where main.hotel_id = info.id
  and ts >= '2021-11-01'
  and ts <= '2021-12-01'
  and tag = 'xb'
  and type is not null
group by type
order by id;

select case when type = '1' then '男' else '女' end as type,
       case when type = '1' then 1 else 2 end     as id,
       sum(value)                                 as value,
       '住宿'                                       as tag
from n_dws_hotel_portrait_d main
         join tr_police_hotel_info info
              on main.hotel_id = info.id
where ts >= '2021-11-01'
  and ts <= '2021-12-01'
  and tag = 'xb'
  and type is not null
group by type
order by id;

SELECT type
FROM n_dws_hotel_portrait_d main,
     tr_police_hotel_info info
WHERE main.hotel_id = info.id
  AND ts >= '2021-11-01'
  AND ts <= '2021-12-01'
  AND tag = 'xb'
  AND type IS NOT NULL
ORDER BY info.id;

select sum(case when main.type = '1' then 1 else 0 end) as type,
       case when main.type = '0' then 1 else 0 end      as id,
       sum(value)                                       as value,
       '住宿'                                             as tag
from n_dws_hotel_portrait_d main,
     tr_police_hotel_info info
where main.hotel_id = info.id
  and ts >= '2021-11-01'
  and ts <= '2021-12-01'
  and tag = 'xb'
  and main.type is not null
group by main.type
order by id;


select count(1), to_char(pub_time, 'yyyy-MM') as mon
from (select hotel_id, pub_time
      from n_dwd_hotel_comment_label
      where pub_time > (select current_date - interval '6 mons')
        and sentiment = 2
        and abstract != '') main,
     (select id from n_dwd_hotel_info where district_id = 330110) info
where main.hotel_id = info.id
group by mon
order by mon desc
limit 6;


select *
from n_dwd_hotel_info info
         join (select occupancy_num::float * 100 as ratio, fusion_id as hotel_id
               from n_dws_hotel_checkin_hotel_day
               where ts::date = (SELECT max(ts) from n_dws_hotel_checkin_hotel_day where district_id = 330110)
                 and district_id = 330110
                 and occupancy_num != '--'
                 and ts >= current_date - interval '100 days') data on info.id = data.hotel_id::int
where district_id = 330110
  and ota_level > 1
  and ratio < 100
order by ratio desc;


select avg(main.price)::int as value, main.price_date
from (select hotel_id, price, price_date
      from n_dwd_hotel_price
      where price_date >= '2021-11-01'
        and price_date <= '2021-12-01') main,
     (select id from n_dwd_hotel_info where district_id = '330110') info
where main.hotel_id = info.id
group by price_date
order by price_date;


SELECT *
from fn_yuhang_reavel_line_tourist_zuiai_line('0', '2021-11-01', '2021-12-01')


SELECT array_agg(a.tour_line)::varchar                              as tour_line,
       avg(a.VALUES)::int                                           AS VALUES,
       json_agg(json_build_object('lng', lng, 'lat', lat))::varchar as weizhi
FROM (
         select a.id, a.tour_line as line, b.name AS tour_line, a.values, nr, lng, lat
         FROM (
             SELECT id, c.tour_line, avg(value)::int AS values, nr
             FROM (
                      select e.*
                      from (
                               SELECT tour_line                                      as tour_lines,
                                      stay_prov,
                                      sum(value)                                     as value,
                                      "row_number"() over (ORDER BY sum(value) desc) as id
                               from n_dwd_scene_population_mobile_travel_line_more_three_scene
                               where come_time::date >= '2021-11-01'::date
                                 and come_time::date <= '2021-12-01'::date
                               GROUP BY tour_line, stay_prov) e
                               inner join
                           (select DISTINCT(code) AS code
                            FROM tr_scene
                            where code is not null
                              and district_id = 330110) b
                           on e.tour_lines::text ~ b.code
                      order by value desc
                      limit 5
                  ) a
                      left join
                  LATERAL unnest(a.tour_lines) WITH ORDINALITY c(tour_line, nr)
                  ON TRUE
             GROUP BY tour_line, id, nr
             ORDER BY id) a

            , (select DISTINCT(code) AS code, name, lng, lat
               FROM tr_scene
               where code is not null) b
         where a.tour_line = b.code
         order by id asc, nr asc
     ) a
GROUP BY id
order by id asc;


select round(COUNT(*)::numeric / value::numeric, 2) as ratio,
       COUNT(*),
       checkin_time + interval '61 days'            as checkin_time
from tr_police_hotel_day_info main,
     (select value, ts
      FROM tr_scene_population_mobile_real
      where obj_id = '330110'
        AND frequency_type = 'DAY'
        and ts between '2021-09-01 00:00:00' and
          '2021-10-25 00:00:00') t
where main.checkin_time = t.ts
  and checkin_time between '2021-09-01 00:00:00' and
    '2021-10-25 00:00:00'
  and district_id = '330110'
group by checkin_time, value;


-- 景区实时客流
select a.name, value, peak, (value / peak::float)::FLOAT as ratio
from (
         SELECT name, value
         from n_dwd_scene_population_mobile_real_adjust
         where ts >= (select max(ts)
                      from n_dwd_scene_population_mobile_real_adjust
                      where ts >= current_timestamp - interval '1 hour'
                        and frequency_type = 'POINT')
           and frequency_type = 'POINT') a
         inner join(
    SELECT name, (extra ->> 'peak') as peak
    from n_dwd_scene_info
    where district_id = 330110
      and type in ('景区', '文化')) b
                   on a.name = b.name
order by ratio desc;


SELECT name,
       future_value,
       CASE
           WHEN future_value > now_value THEN 'up_trend'
           ELSE 'down_trend'
           END as tread,
       CASE
           WHEN (future_value - now_value) * 100::float / now_value > 20 THEN '大于20'
           ELSE '小于20'
           END as amplification
from (
         SELECT b.name, a.value as now_value, c.value as future_value
         from (SELECT name, value
               from n_dwd_scene_population_mobile_real_adjust
               where ts = (select max(ts)
                           from n_dwd_scene_population_mobile_real_adjust
                           where frequency_type = 'POINT'
                             and ts >= current_timestamp - interval '60min')
                 and frequency_type = 'POINT'
               order by value desc) a
                  inner join
              (SELECT code, name from n_dwd_scene_info where district_id = 330110 and code is not null) b
              on a.name = b.name
                  inner join
              (select tfcunit_id, traveller_cnt as value
               from dws_tfc_state_tfcunit_tp_prdtptravellercnt_rt
               where data_step_time_tp = (select max(data_step_time_tp)
                                          from dws_tfc_state_tfcunit_tp_prdtptravellercnt_rt
                                          where data_step_time_tp >= current_timestamp - interval '2 hour')) c
              on b.code = c.tfcunit_id
         order by future_value desc) a
order by future_value desc;

select a.*
from (
         (SELECT scene_name::varchar,
                 to_char(ts, 'YYYY-MM-dd HH24:mi:ss') as ts,
                 checkin_num,
                 (select sum(checkin_num)::int
                  from tr_bianjie_scenic_gate_machine a
                  where frequency_type = 'POINT'
                    and a.ts > CURRENT_DATE
                    and district_name ~ '余杭'
                    and a.ts <= b.ts
                    and a.scene_name = b.scene_name)
          from tr_bianjie_scenic_gate_machine b
          where b.frequency_type = 'POINT'
            and b.ts > CURRENT_DATE + interval '8 H'
            and b.district_name ~ '余杭'
          order by scene_name, ts)

         union all
         (
             select library::varchar                     as scene_name,
                    to_char(ts, 'YYYY-MM-dd HH24:mi:ss') as ts,
                    value,
                    (select sum(value)::int
                     from tr_hanglibrary_flow a
                     where ts > current_date + interval '8 H'
                       and library = '余杭区图书馆'
                       and time_type = 'POINT'
                       and a.ts <= b.ts
                       and a.library = b.library
                    )
             from tr_hanglibrary_flow b
             where ts > current_date + interval '8 H'
               and library = '余杭区图书馆'
               and time_type = 'POINT'
             ORDER BY ts)
         union all
         (
             SELECT scenic::varchar                            as scene_name,
                    to_char(date_str, 'YYYY-MM-dd HH24:mi:ss') as ts,
                    (ticket_num + checkin_num)                 as value,
                    (
                        select COALESCE(sum(ticket_num + checkin_num), 0)::int
                        from tr_bianjie_scenic_point a
                        where date_str > current_date + interval '8 H'
                          and region like '余杭%'
                          and checkin_num > 0
                          and a.scenic = b.scenic
                          and a.date_str < b.date_str
                    )
             from tr_bianjie_scenic_point b
             where date_str > current_date + interval '8 H'
               and region like '余杭%'
               and checkin_num > 0
             order by scenic, date_str
         )
     ) a
where a.scene_name like '%良渚博物院%';


-- select name, code from n_dwd_scene_info where code = 'C10014';
select name, code
from n_dwd_scene_info
where name = '良渚博物院';

select ts as ts, keyword, index_value, 'form' as from, 'to' as to
from tr_trend_baidu_index
where keyword in ('富阳', '余杭', '桐庐', '余杭')
  and ts >= current_date - interval '30 days'
  and ts < current_date
order by ts;


select *
from tr_trend_baidu_index
where keyword in ('富阳', '余杭', '桐庐', '余杭');