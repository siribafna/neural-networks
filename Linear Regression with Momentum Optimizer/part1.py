{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 125,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   symboling normalized_losses         make fuel_type aspiration num_of_doors  \\\n",
      "0          3                 ?  alfa-romero       gas        std          two   \n",
      "1          3                 ?  alfa-romero       gas        std          two   \n",
      "2          1                 ?  alfa-romero       gas        std          two   \n",
      "3          2               164         audi       gas        std         four   \n",
      "4          2               164         audi       gas        std         four   \n",
      "\n",
      "    body_style drive_wheels engine_location  wheel_base  ...  engine_size  \\\n",
      "0  convertible          rwd           front        88.6  ...          130   \n",
      "1  convertible          rwd           front        88.6  ...          130   \n",
      "2    hatchback          rwd           front        94.5  ...          152   \n",
      "3        sedan          fwd           front        99.8  ...          109   \n",
      "4        sedan          4wd           front        99.4  ...          136   \n",
      "\n",
      "   fuel_system  bore  stroke compression_ratio horsepower  peak_rpm city_mpg  \\\n",
      "0         mpfi  3.47    2.68               9.0        111      5000       21   \n",
      "1         mpfi  3.47    2.68               9.0        111      5000       21   \n",
      "2         mpfi  2.68    3.47               9.0        154      5000       19   \n",
      "3         mpfi  3.19     3.4              10.0        102      5500       24   \n",
      "4         mpfi  3.19     3.4               8.0        115      5500       18   \n",
      "\n",
      "  highway_mpg  price  \n",
      "0          27  13495  \n",
      "1          27  16500  \n",
      "2          26  16500  \n",
      "3          30  13950  \n",
      "4          22  17450  \n",
      "\n",
      "[5 rows x 26 columns]\n",
      "\n",
      "Dimensions of data frame: (205, 26)\n"
     ]
    }
   ],
   "source": [
    "### load the data\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "df = pd.read_csv('https://raw.githubusercontent.com/siribafna/CS4372_Assignment_1/master/autos.csv') # data on the web\n",
    "print(df.head())\n",
    "print('\\nDimensions of data frame:', df.shape) # data exploration functions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = df.replace('?', np.nan) # replace all the nulls "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "symboling             0\n",
       "normalized_losses    41\n",
       "make                  0\n",
       "fuel_type             0\n",
       "aspiration            0\n",
       "num_of_doors          2\n",
       "body_style            0\n",
       "drive_wheels          0\n",
       "engine_location       0\n",
       "wheel_base            0\n",
       "length                0\n",
       "width                 0\n",
       "height                0\n",
       "curb_weight           0\n",
       "engine_type           0\n",
       "num_of_cylinders      0\n",
       "engine_size           0\n",
       "fuel_system           0\n",
       "bore                  4\n",
       "stroke                4\n",
       "compression_ratio     0\n",
       "horsepower            2\n",
       "peak_rpm              2\n",
       "city_mpg              0\n",
       "highway_mpg           0\n",
       "price                 4\n",
       "dtype: int64"
      ]
     },
     "execution_count": 128,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum() # how many nulls there are in each column"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Dimensions of data frame: (159, 26)\n"
     ]
    }
   ],
   "source": [
    "df = df.dropna()\n",
    "print('\\nDimensions of data frame:', df.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>symboling</th>\n",
       "      <th>normalized_losses</th>\n",
       "      <th>make</th>\n",
       "      <th>fuel_type</th>\n",
       "      <th>aspiration</th>\n",
       "      <th>num_of_doors</th>\n",
       "      <th>body_style</th>\n",
       "      <th>drive_wheels</th>\n",
       "      <th>engine_location</th>\n",
       "      <th>wheel_base</th>\n",
       "      <th>...</th>\n",
       "      <th>engine_size</th>\n",
       "      <th>fuel_system</th>\n",
       "      <th>bore</th>\n",
       "      <th>stroke</th>\n",
       "      <th>compression_ratio</th>\n",
       "      <th>horsepower</th>\n",
       "      <th>peak_rpm</th>\n",
       "      <th>city_mpg</th>\n",
       "      <th>highway_mpg</th>\n",
       "      <th>price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2</td>\n",
       "      <td>164</td>\n",
       "      <td>audi</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>four</td>\n",
       "      <td>sedan</td>\n",
       "      <td>fwd</td>\n",
       "      <td>front</td>\n",
       "      <td>99.8</td>\n",
       "      <td>...</td>\n",
       "      <td>109</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.19</td>\n",
       "      <td>3.4</td>\n",
       "      <td>10.0</td>\n",
       "      <td>102</td>\n",
       "      <td>5500</td>\n",
       "      <td>24</td>\n",
       "      <td>30</td>\n",
       "      <td>13950</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2</td>\n",
       "      <td>164</td>\n",
       "      <td>audi</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>four</td>\n",
       "      <td>sedan</td>\n",
       "      <td>4wd</td>\n",
       "      <td>front</td>\n",
       "      <td>99.4</td>\n",
       "      <td>...</td>\n",
       "      <td>136</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.19</td>\n",
       "      <td>3.4</td>\n",
       "      <td>8.0</td>\n",
       "      <td>115</td>\n",
       "      <td>5500</td>\n",
       "      <td>18</td>\n",
       "      <td>22</td>\n",
       "      <td>17450</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>1</td>\n",
       "      <td>158</td>\n",
       "      <td>audi</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>four</td>\n",
       "      <td>sedan</td>\n",
       "      <td>fwd</td>\n",
       "      <td>front</td>\n",
       "      <td>105.8</td>\n",
       "      <td>...</td>\n",
       "      <td>136</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.19</td>\n",
       "      <td>3.4</td>\n",
       "      <td>8.5</td>\n",
       "      <td>110</td>\n",
       "      <td>5500</td>\n",
       "      <td>19</td>\n",
       "      <td>25</td>\n",
       "      <td>17710</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>1</td>\n",
       "      <td>158</td>\n",
       "      <td>audi</td>\n",
       "      <td>gas</td>\n",
       "      <td>turbo</td>\n",
       "      <td>four</td>\n",
       "      <td>sedan</td>\n",
       "      <td>fwd</td>\n",
       "      <td>front</td>\n",
       "      <td>105.8</td>\n",
       "      <td>...</td>\n",
       "      <td>131</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.13</td>\n",
       "      <td>3.4</td>\n",
       "      <td>8.3</td>\n",
       "      <td>140</td>\n",
       "      <td>5500</td>\n",
       "      <td>17</td>\n",
       "      <td>20</td>\n",
       "      <td>23875</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>2</td>\n",
       "      <td>192</td>\n",
       "      <td>bmw</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>two</td>\n",
       "      <td>sedan</td>\n",
       "      <td>rwd</td>\n",
       "      <td>front</td>\n",
       "      <td>101.2</td>\n",
       "      <td>...</td>\n",
       "      <td>108</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.5</td>\n",
       "      <td>2.8</td>\n",
       "      <td>8.8</td>\n",
       "      <td>101</td>\n",
       "      <td>5800</td>\n",
       "      <td>23</td>\n",
       "      <td>29</td>\n",
       "      <td>16430</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 26 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "    symboling normalized_losses  make fuel_type aspiration num_of_doors  \\\n",
       "3           2               164  audi       gas        std         four   \n",
       "4           2               164  audi       gas        std         four   \n",
       "6           1               158  audi       gas        std         four   \n",
       "8           1               158  audi       gas      turbo         four   \n",
       "10          2               192   bmw       gas        std          two   \n",
       "\n",
       "   body_style drive_wheels engine_location  wheel_base  ...  engine_size  \\\n",
       "3       sedan          fwd           front        99.8  ...          109   \n",
       "4       sedan          4wd           front        99.4  ...          136   \n",
       "6       sedan          fwd           front       105.8  ...          136   \n",
       "8       sedan          fwd           front       105.8  ...          131   \n",
       "10      sedan          rwd           front       101.2  ...          108   \n",
       "\n",
       "    fuel_system  bore  stroke compression_ratio horsepower  peak_rpm city_mpg  \\\n",
       "3          mpfi  3.19     3.4              10.0        102      5500       24   \n",
       "4          mpfi  3.19     3.4               8.0        115      5500       18   \n",
       "6          mpfi  3.19     3.4               8.5        110      5500       19   \n",
       "8          mpfi  3.13     3.4               8.3        140      5500       17   \n",
       "10         mpfi   3.5     2.8               8.8        101      5800       23   \n",
       "\n",
       "   highway_mpg  price  \n",
       "3           30  13950  \n",
       "4           22  17450  \n",
       "6           25  17710  \n",
       "8           20  23875  \n",
       "10          29  16430  \n",
       "\n",
       "[5 rows x 26 columns]"
      ]
     },
     "execution_count": 130,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head() # data exploration"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = df.drop(columns=['symboling', 'normalized_losses']) # dropping unrelated columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 167,
   "metadata": {},
   "outputs": [],
   "source": [
    "df.make = df.make.astype('category').cat.codes\n",
    "df.fuel_type = df.fuel_type.astype('category').cat.codes\n",
    "df.aspiration = df.aspiration.astype('category').cat.codes\n",
    "df.num_of_doors = df.num_of_doors.astype('category').cat.codes\n",
    "df.body_style = df.body_style.astype('category').cat.codes\n",
    "df.drive_wheels = df.drive_wheels.astype('category').cat.codes\n",
    "df.engine_type = df.engine_type.astype('category').cat.codes\n",
    "df.num_of_cylinders = df.num_of_cylinders.astype('category').cat.codes\n",
    "df.fuel_system = df.fuel_system.astype('category').cat.codes\n",
    "df.bore = df.bore.astype('category').cat.codes\n",
    "df.stroke = df.stroke.astype('category').cat.codes\n",
    "df.horsepower = df.horsepower.astype('category').cat.codes\n",
    "df.peak_rpm = df.peak_rpm.astype('category').cat.codes\n",
    "df.price = df.price.astype('category').cat.codes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 168,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "train size: (127,)\n",
      "test size: (32,)\n"
     ]
    }
   ],
   "source": [
    "# train test split\n",
    "from sklearn.model_selection import train_test_split\n",
    "\n",
    "X = df.iloc[:,9]\n",
    "y = df.iloc[:,10]\n",
    "\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)\n",
    "\n",
    "print('train size:', X_train.shape)\n",
    "print('test size:', X_test.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 169,
   "metadata": {},
   "outputs": [],
   "source": [
    "x = (X_train - X_train.mean()) / X_train.std()\n",
    "x = np.c_[np.ones(X_train.shape[0]), x] "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 174,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Gradient Descent: 54.99, 0.78\n"
     ]
    }
   ],
   "source": [
    "# gradient descent using momentum optimizer\n",
    "lr = .1\n",
    "iterations = 70\n",
    "num_points = y_train.size \n",
    "np.random.seed(123)\n",
    "theta = np.random.rand(2)\n",
    "gamma = .9\n",
    "\n",
    "def gradient_descent(x, y_train, theta, iterations, lr):\n",
    "    costs = []\n",
    "    thetas = [theta] # prev thetas\n",
    "    momentum = 0;\n",
    "    for i in range(iterations):\n",
    "        pred = np.dot(x, theta)\n",
    "        error = pred - y_train\n",
    "        cost = 1/(2*num_points) * np.dot(error.T, error)\n",
    "        costs.append(cost)\n",
    "        momentum = gamma*momentum + (lr * (1/num_points) * np.dot(x.T, error))\n",
    "        theta = theta - momentum\n",
    "        thetas.append(theta)\n",
    "        log.append(theta)\n",
    "        mse.append(mean_squared_error(y, (theta[0]*X + theta[1]))) \n",
    "    return thetas, costs\n",
    "thetas, costs = gradient_descent(x, y_train, theta, iterations, lr)\n",
    "theta = thetas[-1]\n",
    "\n",
    "print(\"Gradient Descent: {:.2f}, {:.2f}\".format(theta[0], theta[1]))\n",
    "y_preds = theta[1]*x + theta[0] "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 175,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# visualizing cost function\n",
    "import matplotlib.pyplot as plt\n",
    "plt.title('Cost Function')\n",
    "plt.xlabel('iterations')\n",
    "plt.ylabel('cost')\n",
    "plt.plot(costs)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 162,
   "metadata": {},
   "outputs": [],
   "source": [
    "x = df.width.to_numpy()\n",
    "y = df.length.to_numpy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 163,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<matplotlib.lines.Line2D at 0x1e86fbe0>,\n",
       " <matplotlib.lines.Line2D at 0x1e86fb68>]"
      ]
     },
     "execution_count": 163,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 720x504 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "plt.figure(figsize=(10,7))\n",
    "plt.scatter(X_train,y_train,s=10, alpha=.5, label='Y')\n",
    "plt.plot(X_train, y_preds)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
